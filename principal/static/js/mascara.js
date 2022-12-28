const email = 'ramkumar@example.com';
const maskEmail = (email = '') => {
   const [name, domain] = email.split('@');
   const { length: len } = name;
   const maskedName = name[0] + '...' + name[len - 1];
   const maskedEmail = maskedName + '@' + domain;
   return maskedEmail;
};
console.log(maskEmail(email));


