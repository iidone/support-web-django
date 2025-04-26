document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/') {
        var footers = document.getElementsByTagName('footer');
        
        if (footers.length > 0) {
            footers[0].style.height = '15.2vh';
        }
    }
});

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/login') {
        var footers = document.getElementsByTagName('footer');
        
        if (footers.length > 0) {
            footers[0].style.height = '15.2vh';
        }
    }
});

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/moder_home') {
        var footers = document.getElementsByTagName('footer');
        
        if (footers.length > 0) {
            footers[0].style.marginTop = '70vh';
            footers[0].style.height = '15.5vh';
        }

        var moderHomeButton = document.getElementById('moderOrBack');
        var moderHomeLink = document.getElementById('moderOrBackLink');

        moderHomeButton.textContent = 'Назад';
        moderHomeLink.onclick = function(event) {
            event.preventDefault();
            history.back();
        }
    }

    if (window.location.pathname === '/moder') {
        var footers = document.getElementsByTagName('footer');
        
        if (footers.length > 0) {
            footers[0].style.marginTop = '60vh';
            footers[0].style.height = '15.5vh';
        }
    }
});

document.addEventListener("DOMContentLoaded", function(){
    if (window.location.pathname === '/control') {
        var controlButton = document.getElementById('controlOrBack');
        var controlButtonLink = document.getElementById('controlOrBackLink');
        
        controlButton.textContent = 'Назад';
        controlButtonLink.onclick = function(event) {
            event.preventDefault();
            history.back();
        };
    }
});

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/moder') {
        var moderHomeButton = document.getElementById('moderOrBack');
        var moderHomeLink = document.getElementById('moderOrBackLink');
        
        moderHomeButton.textContent = 'Назад';
        moderHomeLink.onclick = function(event) {
            event.preventDefault();
            history.back();
        }

        if (footers.length > 0) {
            footers[0].style.marginTop = '20vh';
            footers[0].style.height = '15.5vh';
        }
    }
});

document.addEventListener("DOMContentLoaded", function(){
    if (window.location.pathname === '/form') {
        var admin = document.getElementsByClassName('admin');
        if (admin.length > 0) {
            admin[0].style.visibility = 'hidden';
        }
    }
});

var form1 = document.getElementById('form1');
if (form1){
    form1.addEventListener('submit', (e) => {
        e.preventDefault();

        const isSuccessful = document.getElementById('isSuccessful');
        console.log(isSuccessful);
        isSuccessful.style.visibility = 'visible';
        isSuccessful.style.opacity = 1;

        setTimeout(() => {
            let fadeEffect = setInterval(() => {
                if (isSuccessful.style.opacity > 0) {
                    isSuccessful.style.opacity -= 0.1;
                    console.log(isSuccessful.style.opacity);
                } else {
                    clearInterval(fadeEffect);
                    isSuccessful.style.visibility = 'hidden';
                    form1.submit();
                }
            }, 50);
        }, 1000);
    });
}

var form2 = document.getElementById('form2');
if (form2){
    form2.addEventListener('submit', (e) => {
        e.preventDefault();

        const isSuccessfulAppoint = document.getElementById('isSuccessfulAppoint');
        console.log(isSuccessfulAppoint);
        isSuccessfulAppoint.style.visibility = 'visible';
        isSuccessfulAppoint.style.opacity = 1;

        setTimeout(() => {
            let fadeEffect = setInterval(() => {
                if (isSuccessfulAppoint.style.opacity > 0) {
                    isSuccessfulAppoint.style.opacity -= 0.1;
                    console.log(isSuccessfulAppoint.style.opacity);
                } else {
                    clearInterval(fadeEffect);
                    isSuccessfulAppoint.style.visibility = 'hidden';
                    form2.submit();
                }
            }, 50);
        }, 1000);
    });    
}

