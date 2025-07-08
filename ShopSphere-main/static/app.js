let slider = document.querySelector(".slider-container")
let index = 1 
let dots = document.querySelectorAll(".circle")

const unfill = () =>{
    dots.forEach((elem)=>{
        elem.classList.remove("fill")
    })
}

dots.forEach((elem, sno)=>{
    elem.addEventListener("click", ()=>{
        index = sno
        slider.style.transform = `translateX(${index* -100}vw)`
   
    unfill()
    dots[index].classList.add("fill")
        
    })
})

const slide = () =>{
    if(index==5){
        index = 0
    }
    slider.style.transform = `translateX(${index * -100}vw)`
   
    unfill()
    dots[index].classList.add("fill")
    index++

    
}

setInterval(slide, 5000)

// POSITIONING NAVBAR ON SCROLLING


let nav = document.querySelector("nav")
// window.addEventListener("scroll" , ()=>{
//     nav.style.position = "fixed"
//     nav.style.top = "0"
//     nav.style.left = "0"
//     console.log("l")

// })


let slider1 = document.querySelector(".deal-container")
let index1 = 0 
let dots1 = document.querySelectorAll(".trendcircle")

const trendunfill = () =>{
    dots1.forEach((elem)=>{
        elem.classList.remove("fill")
    })
}
dots1.forEach((elem, sno)=>{
    elem.addEventListener("click", ()=>{
        index1 = sno
        slider1.style.transform = `translateX(${index1* -80}vw)`
   
    trendunfill()
    dots1[index1].classList.add("fill")
        
    })
})
const trendslide = () =>{
    if(index1==3){
        index1 = 0
    }
    slider1.style.transform = `translateX(${index1 * -80}vw)`
   
    trendunfill()
    dots[index1].classList.add("fill")
    index1++

    
}

// let cat = document.querySelector("#categories")
let nav_cat =  document.querySelector(".nav-cat")

// cat.addEventListener("mouseover", ()=>{
//     nav_cat.style.display = "flex"
// })
nav_cat.addEventListener("mouseenter", ()=>{
    nav_cat.style.display = "flex"
})
nav.addEventListener("mouseleave", ()=>{
    nav_cat.style.display = "none"
})
nav_cat.addEventListener("mouseleave", ()=>{
    nav_cat.style.display = "none"
})




if(localStorage.getItem("wcart")== null){
    var cart = {}
}
else{
    var cart = JSON.parse(localStorage.getItem("wcart"))
}

let cards = document.querySelectorAll(".add-cart")

cards.forEach((elem)=>{
    elem.addEventListener("click", ()=>{
        elem.innerHTML = "Added";
        var idstr = elem.id
        console.log(idstr)
        if(cart[idstr]== undefined){
            var qty = 1
            var img_src = document.querySelector(".img"+idstr).src
            var price = document.querySelector(".price"+idstr).innerText
            var name = document.querySelector(".name"+idstr).innerText
            cart[idstr] = [img_src, qty, price, name]
        }
        else{
            cart[idstr][1] += 1
        }
        localStorage.setItem("wcart", JSON.stringify(cart))
        console.log(cart)
        })
        
})


var dest = new Date()
dest.setHours(24, 0, 0, 0)
let hours = document.querySelectorAll(".hour")
let minutes = document.querySelectorAll(".minute")
let seconds = document.querySelectorAll(".second")

setInterval(() => {
    let current = new Date().getTime()
let final = dest - current
if(final < 0){
    final +=  24*60*60*1000
}
let hour = Math.floor((final % (24*60*60*1000)) / (60*60*1000))
if(hour < 10){
    hour = "0" + hour
}
let minute = Math.floor((final % (60*60*1000) / (60*1000)))
if(minute < 10){
    minute = "0" + minute
}
let second = Math.floor((final % (60*1000) / (1000)))
if(second < 10){
    second = "0" + second
}
hours.forEach((elem)=>{
    elem.innerHTML = hour
})
minutes.forEach((elem)=>{
    elem.innerHTML = minute
})
seconds.forEach((elem)=>{
    elem.innerHTML = second
})

}, 1000);



let price_val = document.querySelectorAll(".sort-option")
let sort_val = document.querySelector("#sort-val")
let sort_form = document.querySelector("#sort-form")
price_val.forEach((inpt)=>{
    inpt.addEventListener("change", ()=>{
        if(inpt.checked){
            let val = inpt.value
            sort_val.value = val
            sort_form.submit()
        }
        
    })
})