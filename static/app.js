//code for a copy button

const codes=document.querySelectorAll('pre');
codes.forEach((element)=>{
    var copyButton = document.createElement("span");
    copyButton.innerText = 'Copy';
    copyButton.classList.add("copy-button");
    element.appendChild(copyButton);
    copyButton.addEventListener("click", () => {
        // Hide the copy button temporarily
        copyButton.style.display = "none";

        // Create a range and select the text inside the <pre> tag
        const range = document.createRange();
        range.selectNode(element);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);

        try {
            // Copy the selected text to the clipboard
            document.execCommand("copy");

            // Alert the user that the text has been copied
            copyButton.innerText = "Copied!";
            setTimeout(function(){
                copyButton.innerText = "Copy";
            }, 2000);
        } catch (err) {
            console.error("Unable to copy text:", err);
        } finally {
            // Show the copy button again
            copyButton.style.display = "inline";

            // Deselect the text
            window.getSelection().removeAllRanges();
        }
    });
});

const objects = document.querySelectorAll('p,a,table,div:not(.highlight,.codehilite),img,tr,td, ul,li,ol')
const observer=new IntersectionObserver((entries)=>{
    entries.forEach(
        (entry)=>{
            console.log(entry);
            if (entry.isIntersecting){
                entry.target.classList.add('show')
            }else{
                entry.target.classList.remove('show')
            }
        }
    );

});

objects.forEach((el)=>observer.observe(el));

xss=document.querySelectorAll('kbd,button:not(.nk)')
xss.forEach(element=>{
    element.classList.add('kbc-button')
})

const coords = { x: 0, y: 0 };
const circles = document.querySelectorAll(".circle");

const colors = [
  "#29d246", "#29d246", "#29d246", "#29d246",
  "#29d246", "#29d246", "#29d246", "#29d246"
];

circles.forEach(function (circle, index) {
  circle.x = 0;
  circle.y = 0;
  circle.style.backgroundColor = colors[index % colors.length];
});

window.addEventListener("mousemove", function(e) {
  coords.x = e.clientX;
  coords.y = e.clientY;
});

function animateCircles() {
  let x = coords.x;
  let y = coords.y;

  circles.forEach(function (circle, index) {
    circle.style.left = x - 12 + "px";
    circle.style.top = y - 12 + "px";

    // Use transform for scaling
    circle.style.transform = `scale(${(circles.length - index) / circles.length})`;

    circle.x = x;
    circle.y = y;

    const nextCircle = circles[index + 1] || circles[0];
    x += (nextCircle.x - x) * 0.3;
    y += (nextCircle.y - y) * 0.3;
  });

  requestAnimationFrame(animateCircles);
}

animateCircles();
