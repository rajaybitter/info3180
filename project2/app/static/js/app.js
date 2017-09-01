/* Add your Application JavaScript */

var app = angular.module('web2', []);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);

app.controller('registerController', function($scope, $http, $window){
	$scope.submit = function(){
		var xname = $scope.name;
		var xemail = $scope.email;
		var xpassword = $scope.password;
		var xage = $scope.age;
		var xgender = $scope.gender;
		request = {
			method: 'POST',
			url: "http://localhost:8087/api/users/register",
			headers: {
				'Content-Type': 'application/json'
			},
			data: {name: xname, email: xemail, password: xpassword, age: xage, gender:xgender}
		}

		$http(request).then(function(response){
			alert("Registration successsful");			
			window.location = 'http://localhost:8087/api/users/login'
		}, 
		function(){
			alert("Registration failed")});
	};
});

app.controller('loginController', function($scope, $http, $window, $rootScope){
	$scope.submit = function(){
		var xemail = $scope.email;
		var xpassword = $scope.password;
		request = {
			method: 'POST',
			url: "http://localhost:8087/api/users/login",
			headers: {
				'Content-Type': 'application/json'
			},
			data: {email: xemail, password: xpassword}
		}

		$http(request).then(function(response){
			alert("Login successsful");
			$rootScope.email = $scope.email;
			window.location = 'http://localhost:8087/api/users/home'
		}, 
		function(){
			alert("Login failed")});
	};	
});

app.controller('homeController', function($scope, $rootScope, $http){
	$scope.id = 0;
	$scope.addItem = function(){
		window.location = 'http://localhost:8087/api/users/new_item'
	};
	$scope.getId = function(id){
		request = {
			method: 'GET',
			url: "http://localhost:8087/api/user"
		}
		//alert($rootScope.email);
		$http(request).then(function(response){
			id = response.data['user']['id'];
			$scope.name = response.data['user']['name'];
			request = {
				method: 'GET',
				url: "http://localhost:8087/api/users/"+id+"/wishlist"
			}
			$http(request).then(function successCallback(response){
				$scope.items = response.data['data']['items'];
				console.log($scope.items);
			}, function errorCallback(response){
				alert("Fetching wishlist failed")
			});

		}, 
		function(){
			alert("Request failed")});
			return 0
	};
	
	$scope.getItems = function (id) {
		request = {
			method: 'GET',
			url: "http://localhost:8087/api/users/"+id+"/wishlist"
		}
		$http(request).then(function successCallback(response){
			$scope.items = response.data['data']['items'];
			console.log($scope.items);
		}, function errorCallback(response){
			alert("Fetching wishlist failed")
		});
	};

	$scope.delete = function(id){
		request = {
			method: 'GET',
			url: "http://localhost:8087/api/user"
		}
		//alert($rootScope.email);
		$http(request).then(function(response){
			userid = response.data['user']['id'];
			//$scope.name = response.data['user']['name'];
			request = {
				method: 'DELETE',
				url: "http://localhost:8087/api/users/"+userid+"/wishlist/"+id
			}
			$http(request).then(function successCallback(response){
				
			}, function errorCallback(response){
				alert("Delete failed")
			});

		}, 
		function(){
			alert("Request failed")});
	};

	$scope.getId();		
});

app.controller('itemController', function($scope, $http){
	$scope.submit = function(){
		var xname = $scope.name;
		var xdescription = $scope.description;
		var xurl = $scope.url;
		var xthumbnail_url = $scope.thumbnail_url

		request = {
				method: 'GET',
				url: "http://localhost:8087/api/thumbnails?url="+xthumbnail_url
		}
		$http(request).then(function successCallback(response){
			$scope.urls = response.data['data']['thumbnails'];
		}, function errorCallback(response){
			alert("Thumbnail fetch failed");
		});
	}

	$scope.create = function(url){
		var xname = $scope.name;
		var xdescription = $scope.description;
		var xurl = $scope.url;
		var xthumbnail_url = url

		request = {
			method: 'GET',
			url: "http://localhost:8087/api/user"
		}
		$http(request).then(function(response){
			userid = response.data['user']['id'];
			request = {
				method: 'POST',
				url: "http://localhost:8087/api/users/"+userid+"/wishlist",
				headers: {
					'Content-Type': 'application/json'
				},
				data: {name: xname, description: xdescription, url: xurl,
				 thumbnail_url: xthumbnail_url, owner: userid}
			}
			$http(request).then(function successCallback(response){
				$scope.urls = response.data['data']['thumbnails'];
			}, function errorCallback(response){
				alert("Item creation failed");
			});			
		}, 
		function(){
			alert("Request failed")});
	}

});
