var responsiveHeader = document.querySelector(".responsive-header");
var open = false;

function showMenu() {
    if (open) {
        responsiveHeader.style.height = 0 + "px";
        open = false;
    }else {
        console.log("false");
        responsiveHeader.style.height = "200px";
        open = true;
    }
}
