document.addEventListener("DOMContentLoaded", function () {

    const circles = document.querySelectorAll(".circle");

    circles.forEach(circle => {
        const value = circle.getAttribute("data-value");
        const degree = (value / 100) * 360;

        circle.style.background = 
            `conic-gradient(#667eea ${degree}deg, #ddd ${degree}deg)`;
    });

});