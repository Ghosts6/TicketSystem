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

document.addEventListener("DOMContentLoaded", function () {
  const statusCircles = document.querySelectorAll(".status-circle");

  statusCircles.forEach(circle => {
    const status = circle.dataset.status;

    if (status === 'Pending' || status === 'In Progress') {
      circle.style.backgroundColor = 'yellow';
    } else if (status === 'Completed') {
      circle.style.backgroundColor = 'green';
    } else {
      circle.style.backgroundColor = 'red';
    }

    circle.title = `Ticket Status: ${status}`;
  });
});

document.addEventListener('DOMContentLoaded', function () {
  var page = 2; 

  function loadMoreTickets() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '?page=' + page, true);
    xhr.onload = function () {
      if (xhr.status >= 200 && xhr.status < 400) {
        var container = document.getElementById('ticketList');
        container.innerHTML += xhr.responseText;
        page++;
      }
    };
    xhr.send();
  }

  window.onscroll = function () {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      loadMoreTickets();
    }
  };
});

particlesJS("particles-js", {
  particles: {
    number: { value: 80, density: { enable: true, value_area: 800 } },
    color: { value: "#ffffff" },
    shape: { type: "circle", stroke: { width: 0, color: "#000000" }, polygon: { nb_sides: 5 }, image: { src: "img/github.svg", width: 100, height: 100 } },
    opacity: { value: 0.5, random: false, anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false } },
    size: { value: 3, random: true, anim: { enable: false, speed: 40, size_min: 0.1, sync: false } },
    line_linked: { enable: true, distance: 150, color: "#ffffff", opacity: 0.4, width: 1 },
    move: { enable: true, speed: 6, direction: "none", random: false, straight: false, out_mode: "out", bounce: false, attract: { enable: false, rotateX: 600, rotateY: 1200 } },
  },
  interactivity: {
    detect_on: "canvas",
    events: { onhover: { enable: true, mode: "repulse" }, onclick: { enable: true, mode: "push" }, resize: true },
    modes: { grab: { distance: 400, line_linked: { opacity: 1 } }, bubble: { distance: 400, size: 40, duration: 2, opacity: 8, speed: 3 }, repulse: { distance: 200, duration: 0.4 }, push: { particles_nb: 4 }, remove: { particles_nb: 2 } },
  },
  retina_detect: true,
});
