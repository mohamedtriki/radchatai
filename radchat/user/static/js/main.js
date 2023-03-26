window.addEventListener('load',function(){
    var tl = gsap.timeline();
    tl.to("#loader",{opacity:0,duration:0.7})
    tl.to("#preloader",{opacity:0,duration:0.7})    
    tl.to("#preloader",{display:'none'})   
    tl.fromTo("#title",{opacity:0,y:-20},{opacity:1,duration:0.7,y:0},"-=0.9")    
    tl.fromTo("#description",{opacity:0,y:-20},{opacity:1,duration:0.6,y:0},"-=0.4")    
    tl.fromTo("#btn",{opacity:0,y:-20},{opacity:1,duration:0.6,y:0},"-=0.3")    

})


gsap.fromTo("#cont2_title",{opacity:0,y:-30}, {
    scrollTrigger: {
    trigger: "#cont2",
    start: "30% 90%", 
    },
    opacity:1,y:0,duration:0.8
});
gsap.fromTo("#step1",{opacity:0,y:-20}, {
    scrollTrigger: {
    trigger: "#cont2",
    start: "36% 90%", 

    },
    opacity:1,duration:0.3,y:0 ,delay:0.1});

gsap.fromTo("#step2",{opacity:0,y:-20}, {
    scrollTrigger: {
    trigger: "#cont2",
    start: "36% 90%", 

    },
    opacity:1,duration:0.3,y:0 ,delay:0.2});

gsap.fromTo("#step3",{opacity:0,y:-20}, {
    scrollTrigger: {
    trigger: "#cont2",
    start: "36% 90%", 

    },
    opacity:1,duration:0.3,y:0 ,delay:0.3});


gsap.fromTo("#cont3_p1",{opacity:0,x:-20}, {
    scrollTrigger: {
    trigger: "#cont3",
    start: "36% 90%", 

    },
    opacity:1,duration:0.6,x:0 
});
gsap.fromTo("#cont3_p2",{opacity:0,x:20}, {
    scrollTrigger: {
    trigger: "#cont3",
    start: "56% 90%", 

    },
    opacity:1,duration:0.6,x:0 
});

gsap.fromTo("#cont4_p1",{opacity:0,x:-20}, {
    scrollTrigger: {
    trigger: "#cont4",
    start: "76% 90%", 

    },
    opacity:1,duration:0.6,x:0 
});
gsap.fromTo("#cont4_p2",{opacity:0,x:20}, {
    scrollTrigger: {
    trigger: "#cont4",
    start: "76% 90%", 

    },
    opacity:1,duration:0.6,x:0 
});
// gsap.fromTo("#cont3_p2",{opacity:0,x:20}, {
//     scrollTrigger: {
//     trigger: "#cont3",
//     start: "56% 90%", 

//     },
//     opacity:1,duration:0.9,x:0 
// });




// reports


// plans

$("#plan1").click(function() {
    console.log("working");
    document.getElementById('check_box_cont3').style.backgroundColor="#fefefe"
    document.getElementById('check_box_cont2').style.backgroundColor="#fefefe"
    document.getElementById('check_box_cont1').style.backgroundColor="#163D54"
});

$("#plan2").click(function() {
    document.getElementById('check_box_cont1').style.backgroundColor="#fefefe"
    document.getElementById('check_box_cont3').style.backgroundColor="#fefefe"
    document.getElementById('check_box_cont2').style.backgroundColor="#163D54"
});

$("#plan3").click(function() {
    document.getElementById('check_box_cont2').style.backgroundColor="#fefefe"
    document.getElementById('check_box_cont1').style.backgroundColor="#fefefe"
    document.getElementById('check_box_cont3').style.backgroundColor="#163D54"
});



// signup

document.getElementById('dashboard').addEventListener('click',function(){
      document.getElementById('login_cont').style.opacity=0
      document.getElementById('login_page').style.opacity=0
      document.getElementById('login_page').style.display="flex"
      gsap.fromTo('#login_page',{opacity:0},{opacity:1,duration:0.3})
      gsap.fromTo('#login_cont',{opacity:0,y:20},{opacity:1,y:0,duration:0.3},"=-0.2")
      document.documentElement.style.overflow="hidden";
    })
document.getElementById('btn').addEventListener('click',function(){
      window.scrollTo(0, 0);
      document.getElementById('login_cont').style.opacity=0
      document.getElementById('login_page').style.opacity=0
      document.getElementById('login_page').style.display="flex"
      gsap.fromTo('#login_page',{opacity:0},{opacity:1,duration:0.3})
      gsap.fromTo('#login_cont',{opacity:0,y:20},{opacity:1,y:0,duration:0.3},"=-0.2")
      document.documentElement.style.overflow="hidden";
    })
document.getElementById('cont4_btn').addEventListener('click',function(){
      window.scrollTo(0, 0);
      document.getElementById('login_cont').style.opacity=0
      document.getElementById('login_page').style.opacity=0
      document.getElementById('login_page').style.display="flex"
      gsap.fromTo('#login_page',{opacity:0},{opacity:1,duration:0.3})
      gsap.fromTo('#login_cont',{opacity:0,y:20},{opacity:1,y:0,duration:0.3},"=-0.2")
      document.documentElement.style.overflow="hidden";
    })


document.getElementById('close').addEventListener('click',function(){
    gsap.fromTo('#login_cont',{opacity:1,y:0},{opacity:0,y:20})
      document.getElementById('login_page').style.display="none"
      document.documentElement.style.overflow="scroll";
    })


// login toggle

toggle = document.getElementById('signin_btn')
signup_form = document.getElementById('signup_form')
signin_form = document.getElementById('signin_form')
// if (toggle.innerText =="Log in") {
//     signup_form.style.display="flex"
//     signin_form.style.display="none"
// }
toggle.addEventListener('click',function(){
    if (toggle.innerText =="Log in") {
        signup_form.style.display="none"
        signin_form.style.display="block"
        toggle.innerText='Register'
    }
    else if(toggle.innerText =="Register") {
        signup_form.style.display="block"
        signin_form.style.display="none"
        toggle.innerText='Log in'
    }


})

//     faqs 

document.getElementById('faq').addEventListener('click',function(){
    document.getElementById('faq').style.backgroundColor="#163D54"
})





