function updateClock() {
  const clock = document.getElementById('clock');
  const iranTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Tehran', hour12: false });
  clock.textContent = iranTime.slice(-8);
}

setInterval(updateClock, 1000);

const clockElement = document.getElementById('clock');
const clockMessage = document.getElementById('clockMessage');
let clickCount = 0;

if (clockElement && clockMessage) {
  clockElement.addEventListener('mouseenter', function() {
    clockMessage.style.display = 'block';
  });

  clockElement.addEventListener('mouseleave', function() {
    clockMessage.style.display = 'none';
  });

  clockElement.addEventListener('click', function() {
    clickCount++;
    if (clickCount >= 5) {
      alert(clockMessage.textContent);
      clickCount = 0;
    }
  });
} else {
  console.error("Clock message element not found");
}

document.getElementById('phoneIcon').addEventListener('click', function() {
  const tooltip = document.getElementById('tooltip');
  tooltip.style.display = tooltip.style.display === 'block' ? 'none' : 'block';
});

document.getElementById('submitButton').addEventListener('click', function(event) {
    const inputFields = document.querySelectorAll('input[type="text"], select, textarea');

    let isFormValid = true;

    inputFields.forEach(function(field) {
        if (field.value.trim() === '') {
            isFormValid = false;
            field.style.border = '2px solid red'; 
        } else {
            field.style.border = ''; 
        }
    });

    if (!isFormValid) {
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = 'Fill all the fields';
        errorMessage.style.display = 'block';
        errorMessage.style.color = 'red';
        event.preventDefault();  
    }
});