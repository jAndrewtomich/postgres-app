(function () {
	'use strict';

	angular.module('PgApp', [])

	.controller('PgAppController', ['$scope', '$log',
		function($scope, $log) {
			$scope.getResults = function() {
				$log.log("test");
			};
		};
	]};

}());
