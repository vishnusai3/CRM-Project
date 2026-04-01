from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY
from models import db, User, Product, CartItem, Order, OrderItem, Message, Ticket
from datetime import datetime
from sqlalchemy import func, inspect, text

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)
    with app.app_context():
        db.create_all()
        inspector = inspect(db.engine)
        if 'product' in inspector.get_table_names():
            columns = [col['name'] for col in inspector.get_columns('product')]
            if 'company' not in columns:
                db.session.execute(text('ALTER TABLE product ADD COLUMN company VARCHAR(120)'))
                db.session.commit()
            # Backfill existing products to TechX Nologoe where company is null
            db.session.execute(text("UPDATE product SET company='TechX Nologoe' WHERE company IS NULL"))
            db.session.commit()
        if Product.query.count() == 0:
            products = [
                Product(name='Pro CRM Suite', price=245, description='Complete CRM for teams', company='TechX Nologoe'),
                Product(name='Sales Booster', price=120, description='Sales automation tool', company='TechX Nologoe'),
                Product(name='Support Tracker', price=85, description='Ticketing system add-on'),
                Product(name='Analytics Pro', price=150, description='Reports and dashboards'),
                Product(name='Lead Generator', price=95, description='Automated lead generation'),
                Product(name='Email Campaign Tool', price=110, description='Email marketing suite'),
                Product(name='Customer Insights', price=180, description='Customer behavior analytics'),
                Product(name='Task Manager', price=75, description='Project management tool'),
                Product(name='Invoice Generator', price=60, description='Automated invoicing'),
                Product(name='Data Backup Service', price=40, description='Secure data backup'),
                Product(name='API Integration Kit', price=200, description='Third-party integrations'),
                Product(name='Mobile CRM App', price=130, description='Mobile access to CRM'),
                Product(name='Workflow Automation', price=160, description='Process automation'),
                Product(name='Customer Portal', price=90, description='Self-service portal'),
                Product(name='Reporting Dashboard', price=140, description='Advanced reporting'),
                Product(name='Contact Management', price=50, description='Contact database'),
                Product(name='Event Scheduler', price=70, description='Event planning tool'),
                Product(name='Survey Builder', price=85, description='Customer survey tool'),
                Product(name='Knowledge Base', price=65, description='Help center'),
                Product(name='Chat Support', price=100, description='Live chat integration'),
                Product(name='Social Media Monitor', price=125, description='Social listening'),
                Product(name='SEO Optimizer', price=155, description='Search engine optimization'),
                Product(name='Content Management', price=135, description='CMS integration'),
                Product(name='E-commerce Plugin', price=175, description='Online store integration'),
                Product(name='HR Management', price=190, description='Human resources tool'),
                Product(name='Financial Tracker', price=105, description='Expense tracking'),
                Product(name='Compliance Checker', price=145, description='Regulatory compliance'),
                Product(name='Training Platform', price=115, description='Employee training'),
                Product(name='Video Conferencing', price=80, description='Virtual meetings'),
                Product(name='Document Scanner', price=55, description='OCR scanning'),
                Product(name='Password Manager', price=45, description='Secure password storage'),
                Product(name='Cloud Storage', price=35, description='File storage'),
                Product(name='VPN Service', price=25, description='Secure network access'),
                Product(name='Antivirus Suite', price=30, description='Security software'),
                Product(name='Backup Software', price=50, description='Data recovery'),
                Product(name='Project Planner', price=85, description='Gantt charts'),
                Product(name='Time Tracker', price=40, description='Productivity monitoring'),
                Product(name='Collaboration Tool', price=120, description='Team collaboration'),
                Product(name='Code Repository', price=95, description='Version control'),
                Product(name='Bug Tracker', price=70, description='Issue management'),
                Product(name='Design Tool', price=150, description='Graphic design'),
                Product(name='Video Editor', price=180, description='Video production'),
                Product(name='Audio Recorder', price=65, description='Sound recording'),
                Product(name='Photo Editor', price=90, description='Image editing'),
                Product(name='Translation Service', price=75, description='Language translation'),
                Product(name='Weather App', price=20, description='Weather forecasting'),
                Product(name='News Aggregator', price=15, description='News feed'),
                Product(name='Fitness Tracker', price=100, description='Health monitoring'),
                Product(name='Recipe Manager', price=30, description='Cooking recipes'),
                Product(name='Travel Planner', price=85, description='Trip planning'),
                Product(name='Language Learning', price=60, description='Education app'),
                Product(name='Music Player', price=25, description='Audio streaming'),
                Product(name='Game Platform', price=50, description='Gaming hub'),
                Product(name='Virtual Reality', price=200, description='VR experiences'),
                Product(name='Smart Home Hub', price=120, description='Home automation'),
                Product(name='Drone Controller', price=150, description='Remote piloting'),
                Product(name='AI Assistant', price=175, description='Intelligent automation'),
                Product(name='Blockchain Wallet', price=90, description='Crypto wallet'),
                Product(name='3D Printer', price=300, description='3D printing device'),
                Product(name='Robot Vacuum', price=250, description='Automated cleaning'),
                Product(name='Smart Watch', price=200, description='Wearable tech'),
                Product(name='E-book Reader', price=130, description='Digital reading'),
                Product(name='Streaming Device', price=50, description='Media streaming'),
                Product(name='Wireless Earbuds', price=80, description='Audio accessories'),
                Product(name='Gaming Console', price=400, description='Video gaming'),
                Product(name='Digital Camera', price=350, description='Photography'),
                Product(name='Laptop Stand', price=25, description='Ergonomic accessory'),
                Product(name='Mouse Pad', price=10, description='Computer accessory'),
                Product(name='Keyboard Cover', price=15, description='Protection accessory'),
                Product(name='Screen Protector', price=20, description='Device protection'),
                Product(name='Cable Organizer', price=12, description='Organization tool'),
                Product(name='Desk Lamp', price=40, description='Lighting solution'),
                Product(name='Chair Cushion', price=30, description='Comfort accessory'),
                Product(name='Wall Art', price=60, description='Decorative item')
            ]
            db.session.bulk_save_objects(products)
            db.session.commit()
    return app

app = create_app()

def login_required(role=None):
    def wrapper(fn):
        def decorated(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                return redirect(url_for('login'))
            return fn(*args, **kwargs)
        decorated.__name__ = fn.__name__
        return decorated
    return wrapper

@app.route('/')
def login():
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if 'user_id' in session:
        return redirect(url_for('admin_dashboard') if session['role'] == 'admin' else url_for('customer_dashboard'))
    return render_template('login.html', num1=num1, num2=num2)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if request.method == 'POST':
        # Validate CAPTCHA
        user_num1 = int(request.form.get('num1', 0))
        user_num2 = int(request.form.get('num2', 0))
        user_captcha = int(request.form.get('captcha', 0))
        if user_num1 + user_num2 != user_captcha:
            flash('Invalid CAPTCHA. Please try again.', 'error')
            return render_template('signup.html', num1=num1, num2=num2)
        
        role = request.form.get('role')
        if User.query.filter_by(email=request.form.get('email')).first():
            flash('Email already in use', 'error')
            return render_template('signup.html', num1=num1, num2=num2)
        user = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=generate_password_hash(request.form.get('password')),
            role=role,
            phone=request.form.get('phone'),
            age=request.form.get('age'),
            gender=request.form.get('gender'),
            address=request.form.get('address'),
            work=request.form.get('work'),
            contact=request.form.get('contact'),
            company=request.form.get('company'),
            status='lead'
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', num1=num1, num2=num2)

@app.route('/login', methods=['POST'])
def do_login():
    # Validate CAPTCHA
    user_num1 = int(request.form.get('num1', 0))
    user_num2 = int(request.form.get('num2', 0))
    user_captcha = int(request.form.get('captcha', 0))
    if user_num1 + user_num2 != user_captcha:
        import random
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        flash('Invalid CAPTCHA. Please try again.', 'error')
        return render_template('login.html', num1=num1, num2=num2)
    
    user = User.query.filter_by(email=request.form.get('email')).first()
    if user and check_password_hash(user.password, request.form.get('password')):
        session['user_id'] = user.id
        session['role'] = user.role
        session['name'] = user.name
        session['company'] = user.company if user.company else 'TechX Nologoe'
        return redirect(url_for('admin_dashboard') if user.role == 'admin' else url_for('customer_dashboard'))
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    flash('Invalid credentials', 'error')
    return render_template('login.html', num1=num1, num2=num2)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/customer/dashboard')
@login_required(role='customer')
def customer_dashboard():
    q = request.args.get('q', '')
    products = Product.query.filter(Product.name.ilike(f'%{q}%')).all() if q else Product.query.all()
    return render_template('customer_dashboard.html', products=products, query=q)

@app.route('/customer/profile')
@login_required(role='customer')
def customer_profile():
    user = User.query.get(session['user_id'])
    return render_template('customer_profile.html', user=user)

@app.route('/customer/profile/update', methods=['POST'])
@login_required(role='customer')
def customer_profile_update():
    user = User.query.get(session['user_id'])
    user.name = request.form.get('name')
    user.phone = request.form.get('phone')
    user.age = request.form.get('age')
    user.gender = request.form.get('gender')
    user.address = request.form.get('address')
    user.work = request.form.get('work')
    db.session.commit()
    flash('Profile updated', 'success')
    return redirect(url_for('customer_profile'))

@app.route('/customer/cart/add/<int:product_id>')
@login_required(role='customer')
def add_to_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=session['user_id'], product_id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=session['user_id'], product_id=product_id, quantity=1)
        db.session.add(cart_item)
    db.session.commit()
    flash('Added to cart', 'success')
    return redirect(url_for('customer_dashboard'))

@app.route('/customer/cart')
@login_required(role='customer')
def customer_cart():
    items = CartItem.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in items)
    return render_template('customer_cart.html', items=items, total=total)

@app.route('/customer/cart/remove/<int:item_id>')
@login_required(role='customer')
def remove_cart_item(item_id):
    item = CartItem.query.get(item_id)
    if item and item.user_id == session['user_id']:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('customer_cart'))

@app.route('/customer/checkout', methods=['POST'])
@login_required(role='customer')
def checkout():
    items = CartItem.query.filter_by(user_id=session['user_id']).all()
    if not items:
        flash('Cart is empty', 'error')
        return redirect(url_for('customer_cart'))
    total = sum(item.product.price * item.quantity for item in items)
    order = Order(user_id=session['user_id'], total=total, status='paid', created_at=datetime.utcnow())
    db.session.add(order)
    db.session.flush()
    for item in items:
        order_item = OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, price=item.product.price)
        db.session.add(order_item)
        db.session.delete(item)
    customer = User.query.get(session['user_id'])
    if customer.status in ['lead', 'lost']:
        customer.status = 'converted'
    db.session.commit()
    flash('Purchase completed', 'success')
    return redirect(url_for('customer_orders'))

@app.route('/customer/orders')
@login_required(role='customer')
def customer_orders():
    orders = Order.query.filter_by(user_id=session['user_id']).all()
    return render_template('customer_orders.html', orders=orders)

@app.route('/customer/messages', methods=['GET', 'POST'])
@login_required(role='customer')
def customer_messages():
    if request.method == 'POST':
        admin = User.query.filter_by(role='admin').first()
        receiver_id = admin.id if admin else None
        product_id = request.form.get('product_id')
        content = request.form.get('content')
        if product_id:
            product = Product.query.get(int(product_id))
            content = f"[Product: {product.name}] {content}" if product else content
        message = Message(sender_id=session['user_id'], receiver_id=receiver_id, role='customer', content=content, created_at=datetime.utcnow())
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('customer_messages'))
    messages = Message.query.filter((Message.sender_id == session['user_id']) | (Message.receiver_id == session['user_id'])).order_by(Message.created_at).all()
    products = Product.query.all()
    return render_template('customer_messages.html', messages=messages, products=products)

@app.route('/customer/ticket', methods=['GET', 'POST'])
@login_required(role='customer')
def customer_ticket():
    if request.method == 'POST':
        import os
        from werkzeug.utils import secure_filename
        
        # Handle file upload
        payment_proof_file = request.files.get('payment_proof')
        payment_proof_filename = None
        if payment_proof_file and payment_proof_file.filename:
            filename = secure_filename(payment_proof_file.filename)
            upload_dir = os.path.join(app.root_path, 'static', 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            payment_proof_filename = f"{session['user_id']}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{filename}"
            payment_proof_file.save(os.path.join(upload_dir, payment_proof_filename))
        
        ticket = Ticket(
            product_id=request.form.get('product_id'), 
            customer_id=session['user_id'], 
            issue=request.form.get('issue'), 
            payment_proof=payment_proof_filename, 
            status='open', 
            created_at=datetime.utcnow()
        )
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket submitted', 'success')
        return redirect(url_for('customer_ticket'))
    products = Product.query.all()
    return render_template('customer_ticket.html', products=products)

@app.route('/admin/dashboard')
@login_required(role='admin')
def admin_dashboard():
    total_sales = db.session.query(func.coalesce(func.sum(Order.total), 0)).scalar()
    total_leads = User.query.filter_by(status='lead').count()
    converted = User.query.filter_by(status='converted').count()
    open_tickets = Ticket.query.filter_by(status='open').count()
    chart_data = [total_sales, total_leads, converted, open_tickets]
    return render_template('admin_dashboard.html', total_sales=total_sales, total_leads=total_leads, converted=converted, open_tickets=open_tickets, chart_data=chart_data)

@app.route('/admin/seed-techx-products')
@login_required(role='admin')
def admin_seed_techx_products():
    for i in range(50):
        product = Product(name=f'TechX Generator {i}', price=49.99 + i, description='TechX Nologoe product')
        db.session.add(product)
    db.session.commit()
    flash('Added 50 TechX Nologoe products', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/products', methods=['GET', 'POST'])
@login_required(role='admin')
def admin_products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price') or 0)
        description = request.form.get('description')
        company = request.form.get('company') or 'TechX Nologoe'
        product = Product(name=name, price=price, description=description, company=company)
        db.session.add(product)
        db.session.commit()
        flash('Product added', 'success')
        return redirect(url_for('admin_products'))
    products = Product.query.order_by(Product.name).all()
    return render_template('admin_products.html', products=products)

@app.route('/admin/products/delete/<int:product_id>', methods=['POST'])
@login_required(role='admin')
def admin_delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required(role='admin')
def admin_edit_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('admin_products'))
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.price = float(request.form.get('price') or 0)
        product.description = request.form.get('description')
        product.company = request.form.get('company') or 'TechX Nologoe'
        db.session.commit()
        flash('Product updated', 'success')
        return redirect(url_for('admin_products'))
    return render_template('admin_edit_product.html', product=product)

@app.route('/admin/products/bulk-delete', methods=['POST'])
@login_required(role='admin')
def admin_bulk_delete_products():
    product_ids = request.form.get('product_ids', '').split(',')
    product_ids = [int(pid) for pid in product_ids if pid.strip()]
    if product_ids:
        Product.query.filter(Product.id.in_(product_ids)).delete()
        db.session.commit()
        flash(f'Deleted {len(product_ids)} product(s)', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/products/bulk-update-company', methods=['POST'])
@login_required(role='admin')
def admin_bulk_update_company():
    product_ids = request.form.get('product_ids', '').split(',')
    product_ids = [int(pid) for pid in product_ids if pid.strip()]
    new_company = request.form.get('company')
    if product_ids and new_company:
        Product.query.filter(Product.id.in_(product_ids)).update({'company': new_company})
        db.session.commit()
        flash(f'Updated company for {len(product_ids)} product(s)', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/users')
@login_required(role='admin')
def admin_users():
    users = User.query.filter(User.role=='customer').all()
    return render_template('admin_users.html', users=users)

@app.route('/admin/users/status/<int:user_id>', methods=['POST'])
@login_required(role='admin')
def admin_user_status(user_id):
    user = User.query.get(user_id)
    user.status = request.form.get('status')
    db.session.commit()
    return redirect(url_for('admin_users'))

@app.route('/admin/orders')
@login_required(role='admin')
def admin_orders():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin_orders.html', orders=orders)

@app.route('/admin/tickets')
@login_required(role='admin')
def admin_tickets():
    tickets = Ticket.query.options(db.joinedload(Ticket.customer), db.joinedload(Ticket.product)).order_by(Ticket.created_at.desc()).all()
    return render_template('admin_tickets.html', tickets=tickets)

@app.route('/admin/messages', methods=['GET', 'POST'])
@login_required(role='admin')
def admin_messages():
    if request.method == 'POST':
        message = Message(sender_id=None, receiver_id=request.form.get('customer_id'), role=request.form.get('role'), content=request.form.get('content'), created_at=datetime.utcnow())
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('admin_messages'))
    customers = User.query.filter_by(role='customer').all()
    messages = Message.query.order_by(Message.created_at).all()
    return render_template('admin_messages.html', messages=messages, customers=customers)

@app.route('/admin/messages/<int:customer_id>')
@login_required(role='admin')
def admin_messages_customer(customer_id):
    customer = User.query.get(customer_id)
    messages = Message.query.filter(
        (Message.sender_id == customer_id) | (Message.receiver_id == customer_id)
    ).order_by(Message.created_at).all()
    message_data = []
    for m in messages:
        if m.sender_id == customer_id:
            sender_name = customer.name
        else:
            sender_name = session['name']
        message_data.append({
            'content': m.content,
            'sender_name': sender_name,
            'created_at': m.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return jsonify({'messages': message_data})

@app.route('/admin/notifications')
@login_required(role='admin')
def admin_notifications():
    recent_messages = Message.query.filter(Message.role == 'customer', Message.created_at > datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)).count()
    return jsonify({'new': recent_messages > 0})

if __name__ == '__main__':
    app.run(debug=True)