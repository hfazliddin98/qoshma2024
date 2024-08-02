// SWIPER SLIDER


var swiper = new Swiper(".bg-slider-thumbs", {
    loop: true,
    spaceBetween: 0,
    slidesPerView: 0,
    freeMode: true,
    watchSlidesProgress: true,
});
var swiper2 = new Swiper(".bg-slider", {
    loop: true,
    spaceBetween: 0,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    thumbs: {
        swiper: swiper,
    },
});

//   SCROLL
window.addEventListener("scroll", function() {
    const header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
})

// MOBILE
let navigation = document.querySelector(".navigation");
let menu = document.querySelector(".nav-menu-btn");
let close = document.querySelector(".close-btn");
menu.addEventListener("click", () => {
    navigation.style.display = "flex";
})
close.addEventListener("click", () => {
    navigation.style.display = "none";
})