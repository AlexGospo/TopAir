// Create custom scrollbar div
var scrollbar = document.createElement("div");
scrollbar.style.backgroundColor = "blue";
scrollbar.style.width = "5px";
scrollbar.style.borderRadius = "10px";
scrollbar.style.position = "fixed";
scrollbar.style.right = "0";
scrollbar.style.top = "0";
scrollbar.style.bottom = "0";
document.body.appendChild(scrollbar);

// Track user's scroll position
window.onscroll = function() {
    var scrollPercent = (document.body.scrollTop + document.documentElement.scrollTop) / (document.documentElement.scrollHeight - document.documentElement.clientHeight);
    scrollbar.style.top = (scrollPercent * (document.documentElement.clientHeight - scrollbar.clientHeight)) + "px";
}

