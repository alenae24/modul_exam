let currentSlide = 0;
const slides = document.querySelectorAll(".slide");

function showSlide(index) {
    if (!slides.length) return;

    slides.forEach((slide, i) => {
        slide.style.display = i === index ? "block" : "none";
    });
}

function nextSlide() {
    if (!slides.length) return;

    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    if (!slides.length) return;

    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

if (slides.length) {
    showSlide(currentSlide);
    setInterval(nextSlide, 3000);
}