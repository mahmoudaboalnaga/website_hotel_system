(function() {
    angular.module("hotelreservation.angapp", [])
        .controller("HotelReservation", ["$scope", HotelReservation])
        .controller("CustomerController", ["$scope", Customers]);

    //hotel reservation declaration and add new hotel to the list from input
    function HotelReservation($scope) {
        $scope.hotels = [
            { hotel_name: "Shraton", hotel_city: "Dubai" },
            { hotel_name: "Hilton", hotel_city: "amman" }
        ];
        $scope.add_new_hotel = function(new_hotel, hotels) {
            var hotel = { hotel_name: new_hotel, hotel_city: "any city" };
            hotels.push(hotel);
        };
    }

    //customers function  declaration and add new customers to the list from input
    function Customers($scope) {
        $scope.customers = [
            { customer_name: "Ahmed", customer_mobile: "0100000000" },
            { customer_name: "youssef", customer_mobile: "0100000000" }
        ];
        $scope.add_new_customer = function(new_customer, customers) {
            var newcustomer = { customer_name: new_customer, customer_mobile: "0100000000" };
            customers.push(newcustomer);
        };
    }



})();