// JavaScript for swiping videos and handling actions
console.log("PikOne JS initialized!");

// Example: Handling Like button clicks
document.querySelectorAll(".like-btn").forEach(btn => {
  btn.addEventListener("click", () => alert("Video liked!"));
});
