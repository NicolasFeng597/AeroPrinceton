document.querySelectorAll('.collapsible').forEach(button => {
    button.addEventListener('click', function () {
      this.classList.toggle('active');
  
      const container = this.closest('.container.right');
      if (container) {
        container.classList.toggle('arrow-active', this.classList.contains('active'));
      }
  
      // Toggle collapsible content (optional if using max-height CSS trick)
      const content = this.nextElementSibling;
      if (content.style.maxHeight) {
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  
    // Hover effects for arrow
    button.addEventListener('mouseenter', function () {
      const container = this.closest('.container.right');
      if (container) {
        container.classList.add('arrow-hover');
      }
    });
  
    button.addEventListener('mouseleave', function () {
      const container = this.closest('.container.right');
      if (container) {
        container.classList.remove('arrow-hover');
      }
    });
  });