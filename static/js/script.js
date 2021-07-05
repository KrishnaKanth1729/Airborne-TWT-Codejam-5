
let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-container');
let formClose = document.querySelector('#form-close');
let searchBar = document.getElementById('search');
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navada');
let header = document.querySelector("header")
let loginButton = document.querySelector('#login');
let username = document.querySelector("#username");
let password = document.querySelector('#password');
let inputs = document.getElementsByTagName("input");
let preloader = document.querySelector("#preloader");
let revertButton = document.querySelector("#revert")
let revertButton2 = document.querySelector("#revert-2")


window.addEventListener("load", function(){
    preloader.style.display = 'none';
})
window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove("active");
    loginForm.classList.remove("active");
    header.classList.add("black");
    if(window.pageYOffset == 0) {header.classList.remove("black")}
}

menu.addEventListener("click", () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle("active");
})

formClose.addEventListener('click', () => {
    loginForm.classList.remove('active')
})

let stars = [...document.querySelectorAll(".star")];
let rating = document.querySelector('#rating');

stars.forEach(star => {
    star.addEventListener("mouseover", () => {
        star.classList.add("orange");
        for (const x of Array(parseInt(star.id)).keys()) {
            stars[x].classList.add("orange");
}
    })
})

stars.forEach(star => {
    star.addEventListener("mouseout", () => {
        for (const x of Array(parseInt(star.id)).keys()) {
            stars[x].classList.remove("orange");

}
    })
})

stars.forEach(star => {
    star.addEventListener("click", () => {
        star.classList.add("orange");
        rating.value = star.id
        for (const x of Array(5).keys()) {
            stars[x].classList.remove("fas"); 
            }
        for (const x of Array(parseInt(star.id)).keys()) { 
            stars[x].classList.add("fas");   
            stars[x].classList.add("filled");   

}
    })
})
