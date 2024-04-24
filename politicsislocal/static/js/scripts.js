document.addEventListener('DOMContentLoaded', function () {
    var emailUser = 'cs';
    var emailDomain = 'hamcois.com';
    var emailAddress = emailUser + '@' + emailDomain;
    var emailLink = document.getElementById('emailLink');
    emailLink.href = 'mailto:' + emailAddress;
    emailLink.innerHTML = emailAddress; // This line updates the link text to show the email address
});