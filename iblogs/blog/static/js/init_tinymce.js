document.addEventListener('DOMContentLoaded', function() {
    tinymce.init({
        selector: 'textarea',
        api_key: '1wyjjurj8geks6pfg8cdzra0vmcrxhkkpxg1f6dk906s11dx',  // Replace with your actual API key
        height: 500,
        menubar: false,
        plugins: [
            'advlist autolink lists link image charmap print preview anchor',
            'searchreplace visualblocks code fullscreen',
            'insertdatetime media table paste code help wordcount'
        ],
        toolbar: 'undo redo | formatselect | bold italic backcolor | \
                  alignleft aligncenter alignright alignjustify | \
                  bullist numlist outdent indent | removeformat | help'
    });
});
