$(document).ready(function(){
    $("#key_left").click(function(){
        $.get("/click?key=123", function(data, status){
        });
    });
    $("#key_right").click(function(){
        $.get("/click?key=124", function(data, status){
        });
    });
    $("#key_space").click(function(){
        $.get("/click?key=49", function(data, status){
        });
    });
    $("#key_up").click(function(){
        $.get("/click?key=126", function(data, status){
        });
    });
    $("#key_down").click(function(){
        $.get("/click?key=125", function(data, status){
        });
    });
    $("#app").click(function(){
        $.get("/active?app=搜狐影音", function(data, status){
        });
    });
});
