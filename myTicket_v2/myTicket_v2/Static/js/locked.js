function startTimer(duration, display) {
  let timer = duration, minutes, seconds;
  let interval = setInterval(function () {
    minutes = parseInt(timer / 60, 10);
    seconds = parseInt(timer % 60, 10);

    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    display.textContent = "Countdown: " + minutes + ":" + seconds;

    if (--timer < 0) {
      clearInterval(interval);
      window.location.href = "home/";
    }
  }, 1000);
}

window.onload = function () {
  let fiveMinutes = 60 * 5,
    display = document.querySelector('#timer');
  startTimer(fiveMinutes, display);
};