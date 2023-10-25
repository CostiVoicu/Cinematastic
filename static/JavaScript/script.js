var top_button = document.getElementById("go_top_button");
const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if ((document.body.scrollTop > vh || document.documentElement.scrollTop > vh) && (document.body.offsetWidth > 960 || document.documentElement.offsetWidth > 960)) {
        top_button.style.display = "block";
    } else {
        top_button.style.display = "none";
    }
}

function top_function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

const hamburger_menu = document.querySelector(".hamburger");
const header = document.querySelector("header");
const nav_bar = document.querySelector(".nav_bar_mobile");
const search_mobile = document.querySelector(".search_mobile");
const nav = document.querySelector("nav");
const menu_is_active = () => {
    hamburger_menu.classList.toggle("active");
    header.classList.toggle("header_menu");
    nav_bar.classList.toggle("nav_bar_menu");
    search_mobile.classList.toggle("search_menu");
    nav.classList.toggle("nav_menu");
};
hamburger_menu.addEventListener("click", menu_is_active);