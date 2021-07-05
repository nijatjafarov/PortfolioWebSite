var background = document.querySelector(".background");
var sliders = document.querySelectorAll(".slider");
var slides = document.querySelectorAll(".slide");

background.style.height = document.body.offsetHeight - 16 + 'px';
background.style.width = document.body.offsetWidth - 16 + 'px';

function showSlider(element) {
  var slider = element.parentElement.parentElement.nextElementSibling;
  slider.style.display = "block";
  slider.firstElementChild.style.display = "block";
  background.style.display = "block";
  background.style.opacity = "50%";
  for(var i = 0; i < slider.children.length-1; i++) {
    if(slider.children[i].style.display == "block") {
      currentSlide = i;
      break;
    }
  }
  slider.children[slider.children.length-1].style.top = slider.children[currentSlide].offsetHeight/2 + "px";
  slider.children[0].style.maxHeight = slider.children[0].offsetWidth/3*2 + "px";
}

var currentSlide = 0;

function changeNext(element) {
  var slides = element.parentElement.parentElement.children;
  for(var i = 0; i < slides.length-1; i++) {
    if(slides[i].style.display == "block") {
      currentSlide = i;
      break;
    }
  }

  if(currentSlide == slides.length -2) {
    slides[currentSlide].style.display = "none";
    currentSlide = 0;
    slides[currentSlide].style.display = "block";
    slides[currentSlide].style.maxHeight = slides[currentSlide].offsetWidth/3*2 + "px";
    slides[slides.length-1].style.top = slides[currentSlide].offsetHeight/2 + "px";
  } else {
    slides[currentSlide].style.display = "none";
    slides[currentSlide + 1].style.display = "block";
    slides[currentSlide+1].style.maxHeight = slides[currentSlide+1].offsetWidth/3*2 + "px";
    slides[slides.length-1].style.top = slides[currentSlide+1].offsetHeight/2 + "px";
  }
}

function changePrev(element) {
  var slides = element.parentElement.parentElement.children;
  for(var i = 0; i < slides.length-1; i++) {
    if(slides[i].style.display == "block") {
      currentSlide = i;
      break;
    }
  }
  if(currentSlide == 0) {
    slides[currentSlide].style.display = "none";
    currentSlide = slides.length -2;
    slides[currentSlide].style.display = "block";
    slides[currentSlide].style.maxHeight = slides[currentSlide].offsetWidth/3*2 + "px";
    slides[slides.length-1].style.top = slides[currentSlide].offsetHeight/2 + "px";
  } else {
    slides[currentSlide].style.display = "none";
    slides[currentSlide - 1].style.display = "block";
    slides[currentSlide-1].style.maxHeight = slides[currentSlide-1].offsetWidth/3*2 + "px";
    slides[slides.length-1].style.top = slides[currentSlide-1].offsetHeight/2 + "px";
  }
  
}

function hideBackground(event) {
  if (event.target == background) {
    background.style.opacity = "0";
    background.style.display = "none";

    for(var i = 0; i < sliders.length; i++) {
      sliders[i].style.display = "none";
    }
  }
}

function dynamicSizes() {
  background.style.height = document.body.offsetHeight - 16 + 'px';
  background.style.width = document.body.offsetWidth - 16 + 'px';

  for(var i = 0; i < sliders.length; i++) {
    if(sliders[i].style.display == "block") {
      currentSlider = i;
      break;
    }
  }
  var slidesAndArrows = sliders[currentSlider].children;

  for(var i = 0; i < slidesAndArrows.length-1; i++) {
    slidesAndArrows[i].style.maxHeight = slidesAndArrows[i].offsetWidth/3*2 + "px";
    if(slidesAndArrows[i].style.display == "block") {
      currentSlide = i;
      break;
    }
  }
  slidesAndArrows[slidesAndArrows.length-1].style.top = slidesAndArrows[currentSlide].offsetHeight/2 + "px";
}