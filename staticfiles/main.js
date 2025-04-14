// @ts-ignore
anime({
  targets: ".card",
  translateY: [
    { value: -10, duration: 1000 },
    { value: 0, duration: 1000 },
  ],
  loop: true,
  easing: "easeInOutSine",
});

// @ts-ignore
anime({
  targets: "p",
  opacity: [0, 1],
  translateX: [-200, 0],
  duration: 2000,
  easing: "easeOutExpo",
});

// @ts-ignore
anime({
  targets: ".landing",
  opacity: [0, 1],
  translateY: [-200, 0],
  duration: 4000,
  easing: "easeOutExpo",
});
