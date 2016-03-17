function showImg(){
	url = $('#image_url').val();
	$('.image').html('<img src="' + url + '" class="pure-img">')
}

function showUploadedImg(input){
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('.image').html('<img src="' + e.target.result + '" class="pure-img">')
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function VQA(){
	$('.result').html('<img src="/image/loading.gif" class="pure-img loader">');
    // console.log('Loading...');
    event.preventDefault();
	var formData = new FormData($('#vqa')[0]);

	$.ajax({
        url: '/VQA',
        type: 'POST',
        data: formData,
        success: function (data) {
            data = JSON.parse(data);
            console.log(data);
            answer = data['answer'];
			$('.result').html('Answer:</br><b>'+ answer +'</b>');
        },
        cache: false,
        contentType: false,
        processData: false
    });
}
