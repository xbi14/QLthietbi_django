# Generated by Django 4.2.1 on 2023-05-28 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoaiThietBi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_loaithietbi', models.CharField(max_length=30, verbose_name='Tên loại thiết bị')),
            ],
            options={
                'verbose_name_plural': 'Loại thiết bị',
                'ordering': ['-ten_loaithietbi'],
            },
        ),
        migrations.CreateModel(
            name='Phong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_phong', models.CharField(max_length=30, verbose_name='Tên phòng')),
            ],
            options={
                'verbose_name_plural': 'Phòng',
                'ordering': ['-ten_phong'],
            },
        ),
        migrations.CreateModel(
            name='Tang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_tang', models.CharField(max_length=10, verbose_name='Số tầng')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Tên đăng nhập đã tồn tại.'}, help_text='Yêu cầu 30 ký tự hoặc ít hơn. Chỉ chứa chữ cái, số và các ký tự @/./+/-/_', max_length=30, unique=True, verbose_name='username')),
                ('ho', models.CharField(max_length=30, null=True, verbose_name='Họ')),
                ('ten', models.CharField(max_length=30, null=True, verbose_name='Tên')),
                ('gioi_tinh', models.CharField(choices=[('nam', 'Nam'), ('nu', 'Nữ'), ('khac', 'Khác')], default='Chưa đặt giới tính', max_length=6, null=True, verbose_name='Giới tính')),
                ('chuc_vu', models.CharField(choices=[('quanly', 'Quản Lý'), ('kythuatvien', 'Kỹ Thuật Viên')], default='Chưa đặt chức vụ', max_length=20, null=True, verbose_name='Chức vụ')),
                ('anh_the', models.ImageField(blank=True, null=True, upload_to='anhthe/', verbose_name='Ảnh thẻ')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Địa chỉ email')),
                ('sdt', models.CharField(blank=True, max_length=10, null=True, verbose_name='Số điện thoại')),
                ('ngay_sinh', models.DateField(blank=True, null=True, verbose_name='Ngày sinh')),
                ('ngay_vao_lam', models.DateField(blank=True, null=True, verbose_name='Ngày vào làm')),
                ('is_active', models.BooleanField(default=True, verbose_name='Đang làm việc')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Nhân viên quản lý')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Người dùng',
            },
        ),
        migrations.CreateModel(
            name='ThietBi',
            fields=[
                ('id_thiet_bi', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('ten_thiet_bi', models.CharField(max_length=30, null=True, verbose_name='Tên thiết bị')),
                ('hinh_anh', models.ImageField(null=True, upload_to='anhthietbi/', verbose_name='Hình ảnh')),
                ('ngay_mua', models.DateField(verbose_name='Ngày mua')),
                ('gia_mua', models.IntegerField(verbose_name='Giá mua')),
                ('tinh_trang', models.CharField(choices=[('hoatdong', 'Hoạt động'), ('dangbaotri', 'Đang bảo trì'), ('bihong', 'Bị hỏng')], default='hoatdong', max_length=10, null=True, verbose_name='Tình trạng')),
                ('ngay_bao_tri', models.DateField(blank=True, null=True, verbose_name='Ngày bảo trì')),
                ('mo_ta', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('don_vi_cung_cap', models.CharField(blank=True, max_length=30, null=True, verbose_name='Đơn vị cung cấp')),
                ('loai_thiet_bi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QLthietbi_app.loaithietbi', verbose_name='Loại thiết bị')),
                ('phong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QLthietbi_app.phong', verbose_name='Phòng')),
                ('tang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QLthietbi_app.tang', verbose_name='Tầng')),
            ],
            options={
                'verbose_name_plural': 'Thiết bị',
            },
        ),
        migrations.CreateModel(
            name='QuanLy',
            fields=[
                ('id_nguoidung', models.CharField(blank=True, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id_nguoidung'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='phong',
            name='tang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QLthietbi_app.tang', verbose_name='Tầng'),
        ),
        migrations.CreateModel(
            name='KyThuatVien',
            fields=[
                ('id_nguoidung', models.CharField(blank=True, editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id_nguoidung'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BaoCao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=30, verbose_name='Tiêu đề báo cáo')),
                ('trang_thai', models.CharField(choices=[('dangxuly', 'Đang xử lý'), ('daxuly', 'Đã xử lý')], default='dangxuly', max_length=10, verbose_name='Trạng thái')),
                ('noi_dung', models.TextField(verbose_name='Nội dung')),
                ('ngay_bao_cao', models.DateField(default=django.utils.timezone.now, verbose_name='Ngày báo cáo')),
                ('ngay_bao_cao_disabled', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Ngày báo cáo')),
                ('nguoi_bao_cao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bao_cao_nguoi_bao_cao', to=settings.AUTH_USER_MODEL, verbose_name='Người báo cáo')),
                ('nguoi_bao_cao_disabled', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bao_cao_nguoi_bao_cao_disabled', to=settings.AUTH_USER_MODEL, verbose_name='Người báo cáo')),
                ('nguoi_hoan_thanh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bao_cao_nguoi_hoan_thanh', to=settings.AUTH_USER_MODEL, verbose_name='Người hoàn thành')),
                ('nguoi_nhan_bao_cao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bao_cao_nguoi_nhan_bao_cao', to=settings.AUTH_USER_MODEL, verbose_name='Người nhận báo cáo')),
                ('thiet_bi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QLthietbi_app.thietbi', verbose_name='Thiết bị cần sửa chữa')),
                ('thiet_bi_disabled', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bao_cao_thiet_bi_disabled', to='QLthietbi_app.thietbi', verbose_name='Thiết bị cần sửa chữa')),
            ],
            options={
                'verbose_name_plural': 'Báo cáo',
            },
        ),
    ]
