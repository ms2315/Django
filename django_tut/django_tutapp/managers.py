from django.contrib.auth.base_user import BaseUserManager

class MyUserManager(BaseUserManager):
    
    def create_user(self, username, password = None, **extra_fields):
        if not username:
            raise ValueError("Username is Required")
        
        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if password is None:
            raise ValueError("Superusers must have a password")

        
        return self.create_user(username, password, **extra_fields)