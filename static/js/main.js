// jQuery code to trigger button click on 'Enter' key press
$(document).ready(function() {
    $('.create_task_form input').on('keypress', function(event) {
        if (event.key === 'Enter') {
            // Trigger the button click
            $('.create_task_form button[type=submit]').click();
        }
    });
});