let val = document.querySelector("#quantity").value
let plus = document.querySelector("#plus")
let minus = document.querySelector("#minus")
minus.addEventListener("click",()=>{
    if(val=== 1){
        return
    }
    else{
        val--
        document.querySelector("#quantity").value = val
    }
})
plus.addEventListener("click",()=>{
    val++
    document.querySelector("#quantity").value = val
})

let cols = document.querySelectorAll(".col")
let size = document.querySelectorAll(".si")

const makeAllempty = () => {
    cols.forEach((elem)=>{
        elem.classList.remove("outline")

    })
}
const makeAllSizeEmpty = () => {
    size.forEach((elem)=>{
        elem.classList.remove("outline")

    })
}

cols.forEach((elem)=>{
    elem.addEventListener("click", ()=>{
        makeAllempty()
        elem.classList.add("outline")
    })
})

size.forEach((elem)=>{
    elem.addEventListener("click", ()=>{
        makeAllSizeEmpty()
        elem.classList.add("outline")
    })
})

const stars =document.querySelectorAll(".starLabel")
let rating_val = document.querySelector("#rating-val")

function removestar(){
    stars.forEach((str)=>{
        str.classList.remove("orange")
    })
}
stars.forEach((star, index)=>{
    star.addEventListener("click", ()=>{
        removestar()
        for(let i=0; i<=index; i++){
            stars[i].classList.add("orange")
        }
    })
    
})

let AllStars = document.querySelectorAll(".starInput")
let ratingNum = document.querySelector("#ratingNum")
AllStars.forEach((elem)=>{
    elem.addEventListener("click", (e)=>{
        ratingNum.value = e.target.value
    })
})


// ADDING AD TO CART FUNCTIONALITY 

if(localStorage.getItem("wcart")== null){
    var cart = {}
}
else{
    var cart = JSON.parse(localStorage.getItem("wcart"))
}

let addCartBtn = document.querySelector(".ProdCartBtn")

addCartBtn.addEventListener("click", ()=>{
    addCartBtn.innerText ="Added to cart"
    var idstr = addCartBtn.id
    if(cart[idstr]== undefined){
        var qty = 1
        var img_src = document.querySelector(".img"+idstr).src
        var price = document.querySelector(".price"+idstr).innerText
        cart[idstr] = [img_src, qty, price]
    }
    else{
        cart[idstr][1] += 1
    }
    localStorage.setItem("wcart", JSON.stringify(cart))
    console.log(cart)
})

// PUT DATA INTO DATABASE LIKE SIZE AND COLOR FOR WHICH INPUT TAG IS NOT THERE SO USING JS TO ASSING THE DATA ON CLICK ON ANY OPTION 
document.addEventListener("DOMContentLoaded", ()=>{
    let selectedColor = null
    let selectedSize = null

    document.querySelectorAll(".col").forEach((col)=>{
        col.addEventListener("click", ()=>{
            selectedColor = col.getAttribute("data-colr")
            document.querySelector("#inputColor").value = selectedColor
        })
    })
    document.querySelectorAll(".si").forEach((size)=>{
        size.addEventListener("click", ()=>{
            selectedSize = size.innerText
            document.querySelector("#inputSize").value = selectedSize
        })
    })

    document.querySelector("#orderForm").addEventListener("submit", (e)=>{
        let color = document.querySelector("#inputColor").value
        let size = document.querySelector("#inputSize").value

        if(!color || !size){
            e.preventDefault()
            alert("color and size should be selected")
        }
    })
})