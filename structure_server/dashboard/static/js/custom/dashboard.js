$(document).ready(function() {
  $("student-avatar").mouseenter(function() {
    $(this).css("filter", "");
  }).mouseleave(function() {
    $(this).css("filter", "blur(5px)");
  });
});
