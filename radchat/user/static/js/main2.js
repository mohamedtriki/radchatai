document.getElementById('dash_close').addEventListener('click',function(){
    var tl = gsap.timeline();
    tl.to("#menu",{xPercent:-100,duration:0.3})
    tl.to("#menu",{display:"none",duration:0})

})
document.getElementById('reports_cont').addEventListener('click',function(){
    var tl = gsap.timeline();
    tl.to("#menu",{xPercent:-100,duration:0.3})
    tl.to("#menu",{display:"none",duration:0})

})
document.getElementById('dash_burger').addEventListener('click',function(){
    var tl = gsap.timeline();
    tl.to("#menu",{xPercent:-100,duration:0})
    tl.to("#menu",{display:"flex",duration:0})
    tl.to("#menu",{xPercent:0,duration:0.3})
   
})