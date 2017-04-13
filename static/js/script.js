$(function(){
	$('button').click(function(){
		var date = $('#txtDate').val();
		var time = $('#txtTime').val();
        var macAddress = $('#txtMac').val();
        var clientExist = $('#txtClientExist').val();
        var ipAddress = $('#txtIP').val();
        var internalIP = $('#txtInternalIP').val();
        var knownIP = $('#txtKnownIP').val();
        var userID = $('#txtUserID').val();
        var userExist = $('#txtUserExist').val();
        var loginSuccess = $('#txtLoginSuccess').val();
		$.ajax({
			url: '/log/submit',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});