function toggleAdminFields(){
  const role = document.querySelector('input[name="role"]:checked')?.value;
  const adminFields = document.getElementById('adminFields');
  adminFields.style.display = role === 'admin' ? 'grid' : 'none';
}
function updateRadioSelection(){
  document.querySelectorAll('.radio-option').forEach(option => {
    const radio = option.querySelector('input[type="radio"]');
    if(radio.checked) {
      option.classList.add('selected');
    } else {
      option.classList.remove('selected');
    }
  });
}
window.addEventListener('DOMContentLoaded', ()=>{
  if(document.querySelector('input[name="role"]')) {
    toggleAdminFields();
    updateRadioSelection();
  }
  document.querySelectorAll('input[name="role"]').forEach(radio => {
    radio.addEventListener('change', () => {
      toggleAdminFields();
      updateRadioSelection();
    });
  });
  // Add loading states to forms
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
      const submitBtn = this.querySelector('button[type="submit"]');
      if(submitBtn) {
        submitBtn.classList.add('loading');
        submitBtn.textContent = 'Processing...';
      }
    });
  });
  // Smooth scroll for navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if(target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});
