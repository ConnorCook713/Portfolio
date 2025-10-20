
// Waits for enitre HTML page to load before it begins executing the function
// $ is short for calling the JQuey function
$(document).ready(function() {
    // Function to handle form submission
    $('#login_input').submit(function(event) {
        // Tells code what to do with input data from #source
        // Prevent default form submission
        event.preventDefault();

        // Get the input data from the form with the input field of an id equal to source_request
        var inputData = $('#username').val();

        // Make an AJAX request to the backend
        $.ajax({
            url: '/', // Replace with your backend endpoint
            type: 'POST',
            contentType: 'application/json',
            // source_input is object made to be equal to var inputData. That will be made into JSON and
            // passed to the backend
            data: JSON.stringify({ username: inputData }), // Send input data to the backend as JSON
            success: function(response) {
                // Update the output div with the response from the backend
                // $('#result').text('Response from server: ' + response.message);
                // debug_frontend = response.message;
                // console.log(response.message)

                if (response.message === 'a'){
                    window.location.href = "/query";
                } else {
                    $('#result').html("Invaild Login");
                }
                // Split the response into individual lines
                // var lines = response.message.split('\n');

                // Construct HTML content to display the response
                // += is used to add value to variable that is an integer or to concate two strings together
                //var htmlContent = '';
                //lines.forEach(function(line) {
                    //htmlContent += '<p>' + line + '</p>';
                //});

                // Update the content of the <div> element with id="src_output"
                // $('#src_output').html(htmlContent);
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error('Error:', error);
            }
        });
    });
});


