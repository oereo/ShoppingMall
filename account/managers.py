from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, nickname, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            nickname=nickname,
            phone_number=phone_number,
            # phoneNumber = phoneNumber,
        )
        # user.is_seller = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, nickname, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            nickname=nickname,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user
