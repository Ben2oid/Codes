// Function to fade in the logo when the webpage is loaded
window.addEventListener('load', function() {
    var fadeImage = document.getElementById('main-logo');
    fadeImage.style.opacity = '0'; // Set initial opacity to 0
  
    setTimeout(function() {
      fadeImage.style.transition = 'opacity 0.5s ease'; // Add transition effect
  
      // Check if the page is scrolled to the top
      if (isScrolledToTop()) {
        fadeImage.style.opacity = '1'; // Fade in the logo
      }
    }, 100); // Adjust the delay as needed (in milliseconds)
  });
  
  // Function to check if the page is scrolled to the top
  function isScrolledToTop() {
    return window.pageYOffset === 0;
  }
  
  // Function to handle fading in and out based on scroll position
  var fadeImage = document.getElementById('main-logo');
  
  window.addEventListener('scroll', function() {
    if (isScrolledToTop()) {
      fadeImage.style.opacity = '1'; // Fade in the logo if scrolled to the top
    } else {
      fadeImage.style.opacity = '0'; // Fade out the logo if not scrolled to the top
    }
  });
  
  // Function to handle background color change and scroll position storage
  window.addEventListener('load', function() {
    var body = document.querySelector('body');
    var storedColor = localStorage.getItem('background_color');
    var storedScrollPosition = localStorage.getItem('scroll_position');
  
    if (storedColor) {
      body.style.backgroundColor = storedColor;
    }
  
    if (storedScrollPosition) {
      window.scrollTo(0, parseInt(storedScrollPosition));
    }
  
    window.addEventListener('scroll', function() {
      var scrollPosition = window.scrollY;
      if (scrollPosition > 0) {
        body.style.backgroundColor = 'white';
      } else {
        body.style.backgroundColor = 'black';
      }
      localStorage.setItem('background_color', body.style.backgroundColor);
      localStorage.setItem('scroll_position', scrollPosition);
    });
  });
  
  // Function to handle fading in and out based on scroll position
  var titles = document.getElementsByClassName('titles');
  
  window.addEventListener('scroll', function() {
    var currentScrollPosition = window.pageYOffset;
  
    if (currentScrollPosition === 0) {
      // Scrolled to the top
      for (var i = 0; i < titles.length; i++) {
        titles[i].classList.remove('visible');
      }
    } else {
      // Scrolled away from the top
      for (var i = 0; i < titles.length; i++) {
        titles[i].classList.add('visible');
      }
    }
  });
  