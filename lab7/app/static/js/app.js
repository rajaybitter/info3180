/* Add your Application JavaScript */

var app = angular.module('web2', []);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);

app.controller('scrapeController', function($scope, $http){
		alert("dsfsdfds");
		request = {
			method: 'GET',
			url: "http://localhost:8088/images"
		}
		$http(request).then(function(response){
			$scope.urls = response.data['data']['Thumbnails'];
			alert($scope.urls);
		}, 
		function(response){
			alert("Request failed")});
});