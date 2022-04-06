document.addEventListener("DOMContentLoaded", function () {
  var splide = new Splide("#splide__principal", { rewind: true });
  var splide2 = new Splide("#splide__videos", {
    perPage: 4,
    type: "loop",
    breakpoints: {
      1200: {
        perPage: 3,
      },
      1023: {
        perPage: 2,
      },
      767: {
        perPage: 1,
      },
    },
  });
  splide.mount();
  splide2.mount();
});

var modals = document.querySelectorAll("[data-modal]");

modals.forEach(function (trigger) {
  trigger.addEventListener("click", function (event) {
    event.preventDefault();
    var modal = document.getElementById(trigger.dataset.modal);
    modal.classList.add("open");
    var exits = modal.querySelectorAll(".modal-exit");
    exits.forEach(function (exit) {
      exit.addEventListener("click", function (event) {
        event.preventDefault();
        modal.classList.remove("open");
      });
    });
  });
});
