function open_hamburger() {
   var x = document.getElementById("main_nav");
   if (x.className === "pages") {
     x.className += " mobile";
   } else {
     x.className = "pages";
   }
   console.log("TEST");
 }