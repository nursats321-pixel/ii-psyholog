const textarea = document.querySelector("textarea");

textarea.addEventListener("keydown", function(e){

    if(e.key === "Enter" && !e.shiftKey){

        e.preventDefault();

        document.getElementById("chatForm").submit();

    }

});