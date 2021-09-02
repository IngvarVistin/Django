window.onload = function () {
	$('.basket_list').on('click', 'input[type="number", function ()' {
		var target = event.target;
		console.log(target.name); // id of basket objects
		console.log(target.value); // quantity of basket objects

		$.ajax({
			url: '/baskets/edit/' + target.name + '/' + target.value + '/',
			success: function (data) {
				$('.basket_list').html(data.result);
			},
		}):
	}):
}