$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : JSON.stringify($('#logData').val(), null, '\t'),
			type : 'POST',
			url : '/log/submit'
		})
		.done(function(result) {
            alert(data);
            console.log(result);

		});
    console.log(data);
		event.preventDefault();

	});

});