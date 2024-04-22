function searchFeedback() {
    var input, filter, feedbackItems, div, txtValue;
    input = document.getElementById('searchInput');
    filter = input.value.toUpperCase();
    feedbackItems = document.getElementsByClassName('feedback-item');
    for (var i = 0; i < feedbackItems.length; i++) {
        div = feedbackItems[i];
        txtValue = div.textContent || div.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            div.style.display = "";
        } else {
            div.style.display = "none";
        }
    }
}