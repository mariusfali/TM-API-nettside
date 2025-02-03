// Denne siden er spesifikt til annen type funksjoner enn firebase greiene, de må ligge i HTML fila

let mode_switch = document.getElementById("mode-switch")
let website_body = document.getElementById("html-body")

mode_switch.addEventListener("click", dark_or_light_mode)

function dark_or_light_mode(){
    if (mode_switch.innerText == "Dark mode"){
        mode_switch.innerText = "Light mode"
        website_body.setAttribute("data-theme","dark")
    }
    else{
        mode_switch.innerText = "Dark mode"
        website_body.setAttribute("data-theme","light")
    }
}