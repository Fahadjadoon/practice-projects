const wrapper = document.querySelector('.wrapper');
const loginlink = document.querySelector('.login-link');
const signuplink = document.querySelector('.sign-up-link');
const loginbtn = document.querySelector('.login-btn');
const closeicon = document.querySelector('.close-icon');

//this will add active class to wrapper div
signuplink.addEventListener('click',() =>{
wrapper.classList.add('active');
});

//this will remove active class from wrapper div
loginlink.addEventListener('click',() =>{
wrapper.classList.remove('active');
});

//this will add active-popup class to wrapper div
loginbtn.addEventListener('click',() =>{
wrapper.classList.add('active-popup');
});

//this will remove active-popup class from wrapper div
closeicon.addEventListener('click',() =>{
wrapper.classList.remove('active-popup');
});