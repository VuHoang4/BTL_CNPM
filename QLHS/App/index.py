from App import app, login_manager, dao,db
from flask import render_template, redirect, request, jsonify, request, url_for, flash, session
from flask_login import login_user,current_user,logout_user
from App.models import NguoiDung, VaiTro,Khoi, LoaiDiem,LoaiQuyDinh,MonHoc,HocKy,Lop,HocSinhLop,HocSinh,LopMonHoc,Diem
from datetime import date, datetime,timedelta
from werkzeug.security import hashlib


import random
import string
import logging

@app.route("/")
def index():

    # def generate_random_username():
    #     return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    #
    # def generate_random_name():
    #     first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng"]
    #     last_names = ["An", "Bình", "Cường", "Đức", "Hải"]
    #     return f"{random.choice(first_names)} {random.choice(last_names)}"
    #
    # def generate_random_email(username):
    #     domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    #     return f"{username}@{random.choice(domains)}"
    #
    # # Tạo 30 người dùng với vai trò giáo viên
    # for _ in range(30):
    #     ten_dang_nhap = generate_random_username()
    #     mat_khau = "1234"  # Mật khẩu mặc định
    #     vai_tro =VaiTro.GIAOVIEN  # Vai trò giáo viên
    #     ten_nguoi_dung = generate_random_name()
    #     email = generate_random_email(ten_dang_nhap)
    #     avatar = None  # Có thể thay đổi avatar nếu cần
    #
    #     dao.add_nguoi_dung(ten_dang_nhap, mat_khau, vai_tro, ten_nguoi_dung, email, avatar)
    #
    # dao.add_nguoi_dung('admin', "123456", VaiTro.QUANTRI, 'Admin', 'vuhoang@gmail')


    # def generate_random_name():
    #     first_names = ["An", "Bình", "Cường", "Đức", "Hải", "Khoa", "Linh", "Mai", "Nam", "Oanh"]
    #     return random.choice(first_names)
    #
    # def generate_random_surname():
    #     surnames = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đỗ", "Ngô", "Bùi", "Dương"]
    #     return random.choice(surnames)
    #
    # def generate_random_email(username):
    #     domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    #     return f"{username}@{random.choice(domains)}"
    #
    # def generate_random_phone_number():
    #     return "0" + ''.join(random.choices(string.digits, k=9))
    #
    # def generate_random_address():
    #     streets = ["Đường 1", "Đường 2", "Đường 3", "Đường 4", "Đường 5"]
    #     return f"{random.choice(streets)}, Thành phố {random.choice(['Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng'])}"
    #
    # def generate_random_birth_date():
    #     start_date = datetime(2005, 1, 1)
    #     end_date = datetime(2010, 12, 31)
    #     return start_date + (end_date - start_date) * random.random()
    #
    # # Tạo 50 học sinh
    # for _ in range(50):
    #     ho = generate_random_surname()
    #     ten = generate_random_name()
    #     ngay_sinh = generate_random_birth_date().date()
    #     email = generate_random_email(ho.lower() + ten.lower())
    #     gioi_tinh = random.choice(["Nam", "Nữ"])
    #     so_dien_thoai = generate_random_phone_number()
    #     dia_chi = generate_random_address()
    #     khoi = random.choice(list(Khoi))  # Chọn ngẫu nhiên khối lớp
    #
    #     dao.add_hoc_sinh(ho, ten, ngay_sinh, email, gioi_tinh, so_dien_thoai, dia_chi, khoi)
    # def create_hoc_ky():
    #     hoc_ky_info = [
    #         ("Học Kỳ 1", "2023-2024"),
    #         ("Học Kỳ 2", "2023-2024"),
    #         ("Học Kỳ 1", "2024-2025"),
    #         ("Học Kỳ 2", "2024-2025"),
    #         ("Học Kỳ 1", "2025-2026"),
    #         ("Học Kỳ 2", "2025-2026"),
    #         ("Học Kỳ 1", "2026-2027"),
    #         ("Học Kỳ 2", "2026-2027"),
    #         ("Học Kỳ 1", "2027-2028"),
    #         ("Học Kỳ 2", "2027-2028"),
    #     ]
    #
    #     for ten_hoc_ky, nam_hoc in hoc_ky_info:
    #         dao.add_hoc_ky(ten_hoc_ky, nam_hoc)

    # # Gọi hàm để tạo 10 học kỳ
    # create_hoc_ky()
    # Kiểm tra xem người dùng đã đăng nhập hay chưa
    # Dữ liệu cần thêm
    # maLop = "LH12001"
    # maMonHocs = ["CN1004", "HH1003", "NV1005", "TH001", "VL1002"]
    # maGVBMs = ["GVB8FF3D07", "GVDF27418C", "GVE3B7630F", "GVF0240174", "GVB8FF3D07"]
    #
    # # Thêm các môn học vào lớp
    # for i in range(len(maMonHocs)):
    #     dao.add_mon_hoc_vao_lop(maLop, maMonHocs[i], maGVBMs[i])

    # # Dữ liệu cần thêm
    # maMonHoc = "TH1001"
    # maHocSinh = [
    #     "HS240006", "HS240007", "HS240008", "HS240009", "HS240011",
    #     "HS240012", "HS240016", "HS240022", "HS240025", "HS240028",
    #     "HS240038", "HS240039", "HS240041", "HS240031", "HS240032",
    #     "HS240044", "HS240051", "HS240054", "HS240056", "HS240059",
    #     "HS240061", "HS240065", "HS240069", "HS240078"
    # ]
    # maHocKy = "2401"
    #
    # # Thêm điểm cho từng học sinh
    # for ma_hoc_sinh in maHocSinh:
    #     print(f"Thêm điểm cho học sinh: {ma_hoc_sinh}")
    #
    #     # 1 điểm MIENG
    #     # dao.add_diem(dao.generate_random_score(), LoaiDiem.MIENG, maMonHoc, ma_hoc_sinh, maHocKy)
    #
    #     # 3 điểm PHUT_15
    #     for _ in range(3):
    #         dao.add_diem(dao.generate_random_score(), LoaiDiem.PHUT_15, maMonHoc, ma_hoc_sinh, maHocKy)
    #
    #     # 2 điểm TIET_1
    #     for _ in range(2):
    #         dao.add_diem(dao.generate_random_score(), LoaiDiem.TIET_1, maMonHoc, ma_hoc_sinh, maHocKy)
    #
    #     # 1 điểm GIUA_KI
    #     dao.add_diem(dao.generate_random_score(), LoaiDiem.GIUA_KI, maMonHoc, ma_hoc_sinh, maHocKy)
    #
    #     # 1 điểm CUOI_KI
    #     dao.add_diem(dao.generate_random_score(), LoaiDiem.CUOI_KI, maMonHoc, ma_hoc_sinh, maHocKy)
    #
    # print("Đã thêm điểm thành công.")
    # # Danh sách các mã lớp
    # maLops = ['LH12001', 'LH12002']
    #
    # # Mã môn học
    # maMonHoc = 'TH1001'
    #
    # # Danh sách mã giáo viên
    # maGVBMs = ['GV0FBDBC9B', 'GV1331674F']
    #
    # # Gọi hàm để thêm cho từng mã lớp và từng giáo viên
    # for maLop in maLops:
    #     for maGVBM in maGVBMs:
    #         dao.add_mon_hoc_vao_lop(maLop, maMonHoc, maGVBM)

    if not current_user.is_authenticated:
        return redirect("/login")  # Chuyển tới trang login nếu chưa đăng nhập
    return redirect("/dashboard")  # Hiển thị trang index nếu đã đăng nhập


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tenDangNhap = request.form['username']
        matKhau = request.form['password']


        user = dao.auth_user(username=tenDangNhap, password=matKhau)

        if user :  # Kiểm tra mật khẩu
            login_user(user)
            return redirect(url_for('dashboard'))  # Chuyển hướng đến trang dashboard

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    user_role = current_user.vaiTro

    if user_role == VaiTro.GIAOVIEN:
        return render_template('giaovien_dashboard.html')
    elif user_role == VaiTro.GIAOVU:
        return render_template('giaovu_dashboard.html')

    return render_template('default_dashboard.html')

@app.route("/logout", methods=['get', 'post'])
def logout_process():
    logout_user()
    return redirect("/login")


@app.route("/login-admin", methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')
    u = dao.auth_user(username=username, password=password, role=VaiTro.QUANTRI)
    if u:
        login_user(u)

    return redirect('/admin')

@login_manager.user_loader
def load_user(maNguoiDung):
    return NguoiDung.query.get(maNguoiDung)  # Lấy người dùng từ cơ sở dữ liệu theo maNguoiDung


@app.route('/user/<string:tenDangNhap>')
def user_profile(tenDangNhap):
    # Tìm người dùng theo tên đăng nhập
    user = NguoiDung.query.filter_by(tenDangNhap=tenDangNhap).first()
    if user:
        return render_template('user_profile.html', user=user)
    else:
        return "Người dùng không tồn tại", 404


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user = current_user

    if request.method == 'POST':
        tenDangNhap = request.form['tenDangNhap']
        matKhau = request.form['matKhau']
        matKhauConfirm = request.form['matKhauConfirm']
        tenNguoiDung = request.form['tenNguoiDung']
        email = request.form['email']
        avatar = request.form['avatar']

        # Kiểm tra tính duy nhất của email
        existing_user = NguoiDung.query.filter_by(email=email).first()
        if existing_user and existing_user.maNguoiDung != user.maNguoiDung:
            flash('Email đã được sử dụng bởi người dùng khác!', 'danger')
            return redirect(url_for('edit_profile'))

            # Kiểm tra xem mật khẩu có được thay đổi không
        if matKhau and matKhau != "**********":
            # Kiểm tra khớp mật khẩu
            if matKhau != matKhauConfirm:
                flash('Hai mật khẩu không khớp, vui lòng thử lại!', 'danger')
                return redirect(url_for('edit_profile'))
            user.matKhau = hashlib.md5(matKhau.encode('utf-8')).hexdigest()  # Mã hóa mật khẩu

        # Cập nhật thông tin người dùng
        user.tenDangNhap = tenDangNhap
        user.tenNguoiDung = tenNguoiDung
        user.email = email
        user.avatar = avatar

        db.session.commit()
        flash('Thông tin của bạn đã được cập nhật!', 'success')
        return redirect(url_for('user_profile', tenDangNhap=user.tenDangNhap))

    return render_template('edit_profile.html', user=user)



# API lấy danh sách khối
@app.route('/api/khois', methods=['GET'])
def get_khois():
    khois = [k.value for k in Khoi]
    return jsonify(khois)

# API lấy danh sách lớp theo khối
# API lấy danh sách lớp theo khối
@app.route('/api/classes', methods=['GET'])
def get_classes():
    grade = request.args.get('grade', type=int)
    year = request.args.get('year', type=str)  # Lấy năm học từ tham số
    classes = db.session.query(Lop).join(HocSinhLop).filter(
        HocSinhLop.namHoc == year,
        Lop.khoi == Khoi(grade)
    ).all()
    return jsonify([{'maLop': lop.maLop, 'tenLop': lop.tenLop} for lop in classes])

# API lấy danh sách môn học
@app.route('/api/subjects', methods=['GET'])
def get_subjects():
    maLop = request.args.get('classId', type=str)  # Lấy mã lớp từ tham số
    subjects = db.session.query(MonHoc).join(LopMonHoc).filter(LopMonHoc.maLop == maLop).all()
    return jsonify([{'maMonHoc': mon.maMonHoc, 'tenMonHoc': mon.tenMonHoc} for mon in subjects])

# API lấy danh sách học kỳ
@app.route('/api/hocky', methods=['GET'])
def get_hocky():
    year = request.args.get('year', type=str)  # Lấy năm học từ tham số
    hocky = HocKy.query.filter_by(namHoc=year).all()
    return jsonify([{'maHocKy': hk.maHocKy, 'tenHocKy': hk.tenHocKy, 'namHoc': hk.namHoc} for hk in hocky])

@app.route('/add_hoc_sinh', methods=['POST'])
def add_hoc_sinh():
    data = request.json
    ho = data.get('ho')
    ten = data.get('ten')
    ngay_sinh = data.get('ngay_sinh')
    email = data.get('email')
    gioi_tinh = data.get('gioi_tinh')
    so_dien_thoai = data.get('so_dien_thoai')
    dia_chi = data.get('dia_chi')
    khoi=Khoi(int(data.get('khoi')))
    print(khoi)

    errors = []

    # Kiểm tra email đã tồn tại chưa
    if dao.check_email_exists(email):
        errors.append("Email đã tồn tại trong cơ sở dữ liệu.")

    # Kiểm tra số điện thoại đã tồn tại chưa
    if dao.check_phone_exists(so_dien_thoai):
        errors.append("Số điện thoại đã tồn tại trong cơ sở dữ liệu.")

    # Tính tuổi từ ngày sinh
    today = datetime.today()
    ngay_sinh_date = datetime.strptime(ngay_sinh, "%Y-%m-%d")  # Định dạng ngày tháng

    age = today.year - ngay_sinh_date.year - ((today.month, today.day) < (ngay_sinh_date.month, ngay_sinh_date.day))

    # Lấy quy định tuổi tối thiểu và tối đa mới nhất
    quy_dinh_toi_thieu = dao.get_most_recent_quy_dinh("TUOI_TOI_THIEU")
    quy_dinh_toi_da = dao.get_most_recent_quy_dinh("TUOI_TOI_DA")

    # Kiểm tra quy định tuổi tối thiểu
    if quy_dinh_toi_thieu and age < quy_dinh_toi_thieu.giaTri:
        errors.append(f"Tuổi tối thiểu là {quy_dinh_toi_thieu.giaTri}.")

    # Kiểm tra quy định tuổi tối đa
    if quy_dinh_toi_da and age > quy_dinh_toi_da.giaTri:
        errors.append(f"Tuổi tối đa là {quy_dinh_toi_da.giaTri}.")

    # Nếu có lỗi, trả về thông báo lỗi
    if errors:
        return jsonify({"errors": errors}), 400

    # Nếu không có lỗi, thêm học sinh vào DB
    dao.add_hoc_sinh(ho, ten, ngay_sinh, email, gioi_tinh, so_dien_thoai, dia_chi,khoi)

    return jsonify({"message": "Học sinh đã được thêm thành công!"}), 201


# api get HocSinh
@app.route('/api/students', methods=['GET'])
def get_students():
    grade = request.args.get('grade', type=int)
    year = request.args.get('year', type=str)  # Lấy năm học từ tham số
    # print(year)

    if grade in [10, 11, 12]:
        # Lấy danh sách học sinh theo khối
        students = dao.get_students_by_grade(grade)

        # Lấy danh sách mã học sinh trong lớp học sinh
        lophocsinh = dao.get_students_in_classes()  # Giả sử đây là hàm lấy dữ liệu lớp học sinh
        maHocSinh_lophoc = {student['maHocSinh'] for student in lophocsinh}  # Tạo tập hợp mã học sinh trong lớp

        # Lọc học sinh
        filtered_students = []
        for student in students:
            if student['maHocSinh'] not in maHocSinh_lophoc:
                filtered_students.append(student)
            else:
                # Kiểm tra năm học
                student_class_year = next(
                    (cls['namHoc'] for cls in lophocsinh if cls['maHocSinh'] == student['maHocSinh']), None)
                if student_class_year != year:
                    filtered_students.append(student)

        return jsonify(filtered_students)

    return jsonify([])

# API Để Lấy Kỳ Học
@app.route('/api/semesters', methods=['GET'])
def get_semesters():
    semesters = dao.get_all_semesters()  # Lấy tất cả kỳ học từ cơ sở dữ liệu
    return jsonify(semesters)

# API Để Lấy Giáo Viên
@app.route('/api/teachers', methods=['GET'])
def get_teachers():
    selected_year = request.args.get('year',  type=str)  # Lấy năm học từ yêu cầu
    print('nam: ')
    print(selected_year)

    # Lấy danh sách giáo viên không thuộc lớp có học sinh trong năm học đã chọn
    teachers_in_classes = dao.get_teachers_in_classes(selected_year)

    # Lấy tất cả giáo viên
    teachers = dao.get_all_teachers()

    # Lọc giáo viên
    filtered_teachers = [teacher for teacher in teachers if teacher['maNguoiDung'] not in teachers_in_classes]

    return jsonify(filtered_teachers)




# 3 API để Luu trong LapDSLop
@app.route('/api/lop', methods=['POST'])
def add_lop_api():
    data = request.json
    try:
        maLop = dao.generate_ma_lop(Khoi(int(data['khoi'])))

        # Lấy quy định sĩ số tối đa mới nhất
        quy_dinh_si_so_toi_da = dao.get_most_recent_quy_dinh("SI_SO_TOI_DA")
        print(quy_dinh_si_so_toi_da.giaTri)

        # Kiểm tra quy định sĩ số
        siSo = int(data['siSo'])
        print(siSo)
        errors = []

        if quy_dinh_si_so_toi_da and siSo > quy_dinh_si_so_toi_da.giaTri:
            errors.append(f"Sĩ số tối đa là {quy_dinh_si_so_toi_da.giaTri}.")

        if errors:
            return jsonify({'errors': errors}), 400  # Trả về mã lỗi 400 nếu có lỗi

        # Gọi hàm add_lop đã có
        dao.add_lop(
            maLop=maLop,
            tenLop=data['tenLop'],
            siSo=siSo,
            khoi=Khoi(int(data['khoi'])),
            maGVCN=data.get('maGVCN')
        )

        return jsonify({'maLop': maLop, 'message': 'Lớp đã được thêm thành công.'}), 201
    except Exception as e:
        logging.error(f"Lỗi khi thêm lớp: {str(e)}")
        return jsonify({'message': 'Đã xảy ra lỗi, vui lòng thử lại.'}), 500


@app.route('/api/hoc-ky', methods=['POST'])
def add_hoc_ky_api():
    data = request.json
    try:
        # Kiểm tra xem học kỳ đã tồn tại
        existing_semester = HocKy.query.filter_by(namHoc=data['nam_hoc'], tenHocKy=data['ten_hoc_ky']).first()
        if existing_semester:
            return jsonify({'message': 'Kỳ học đã tồn tại.'}), 409  # 409 Conflict

        # Gọi hàm để thêm kỳ học
        dao.add_hoc_ky(
            ten_hoc_ky=data['ten_hoc_ky'],
            nam_hoc=data['nam_hoc']
        )
        return jsonify({'message': 'Kỳ học đã được thêm thành công.'}), 201
    except Exception as e:
        logging.error(f"Lỗi khi thêm kỳ học: {str(e)}")
        return jsonify({'message': 'Đã xảy ra lỗi, vui lòng thử lại.'}), 500


@app.route('/api/hoc-sinh-lop', methods=['POST'])
def add_hoc_sinh_vao_lop_api():
    data = request.json
    maHocSinh = data['maHocSinh']
    maLop = data['maLop']
    namHoc=data['namHoc']
    print(maLop)

    # Gọi hàm đã có để thêm học sinh vào lớp
    try:
        existing_record = HocSinhLop.query.filter_by(maHocSinh=maHocSinh, maLop=maLop, namHoc=namHoc).first()
        if existing_record:
            logging.warning(f"Học sinh {maHocSinh} đã được ghi danh vào lớp {maLop} trong kỳ học {namHoc}.")
            return jsonify({
                               'message': f'Học sinh {maHocSinh} đã được ghi danh vào lớp {maLop} trong kỳ học {namHoc}.'}), 409  # 409 Conflict

        dao.add_hoc_sinh_vao_lop(maHocSinh, maLop,namHoc)  # Gọi hàm đã có
        return jsonify({'message': 'Học sinh đã được thêm vào lớp'}), 201

    except Exception as e:
        logging.error(f"Lỗi khi thêm học sinh vào lớp: {str(e)}")
        return jsonify({'message': 'Đã xảy ra lỗi, vui lòng thử lại.'}), 500

#QLHS
@app.route('/api/manage_students', methods=['GET'])
def get_manage_students():
    student_id = request.args.get('studentId')
    print(student_id)

    # Tìm kiếm học sinh theo mã học sinh
    student = HocSinh.query.filter_by(maHocSinh=student_id).first()
    print(student.email)

    if student:
        return jsonify({
            'maHocSinh': student.maHocSinh,
            'ho': student.ho,
            'ten': student.ten,
            'ngaySinh': student.ngaySinh.strftime('%Y-%m-%d'),  # Chuyển đổi định dạng ngày
            'email': student.email,
            'gioiTinh': student.gioiTinh,
            'soDienThoai': student.soDienThoai,
            'diaChi': student.diaChi,
            'khoi': student.khoi.value
        })
    else:
        return jsonify({'message': 'Không tìm thấy học sinh1.'}), 404

@app.route('/api/update_students', methods=['POST'])
def update_students():
    updated_students = request.json
    for student_data in updated_students:
        student = HocSinh.query.filter_by(maHocSinh=student_data['maHocSinh']).first()
        if student:
            student.ho = student_data['ho']
            student.ten = student_data['ten']
            student.ngaySinh = student_data['ngaySinh']
            student.email = student_data['email']
            student.gioiTinh = student_data['gioiTinh']
            student.soDienThoai = student_data['soDienThoai']
            student.diaChi = student_data['diaChi']
            db.session.commit()
    return jsonify({'status': 'success'})
# HET QLHS

#
@app.route('/api/list_classes', methods=['GET'])
def list_classes():
    academic_year = request.args.get('academicYear')
    grade = request.args.get('grade')

    try:
        # Lấy danh sách lớp theo năm học và khối
        classes = db.session.query(Lop).join(HocSinhLop).filter(
            HocSinhLop.namHoc == academic_year,
            Lop.khoi == Khoi(int(grade))
        ).all()

        result = [{'maLop': c.maLop, 'tenLop': c.tenLop, 'siSo': c.siSo} for c in classes]
        return jsonify(result)
    finally:
        db.session.close()

@app.route('/api/class/<class_id>', methods=['GET'])
def get_class_details(class_id):
    try:
        class_data = db.session.query(Lop).filter(Lop.maLop == class_id).first()
        if not class_data:
            return jsonify({'error': 'Class not found'}), 404

        students = db.session.query(HocSinhLop).filter(HocSinhLop.maLop == class_id).all()
        student_details = [
            {
                'maHocSinh': s.maHocSinh,
                'ho': db.session.query(HocSinh).filter(HocSinh.maHocSinh == s.maHocSinh).first().ho,
                'ten': db.session.query(HocSinh).filter(HocSinh.maHocSinh == s.maHocSinh).first().ten
            }
            for s in students
        ]

        return jsonify({
            'tenLop': class_data.tenLop,
            'siSo': class_data.siSo,
            'hocSinh': student_details
        })
    finally:
        db.session.close()

@app.route('/api/delete_student', methods=['POST'])
def remove_student():
    data = request.json
    student_id = data.get('studentId')
    class_id = data.get('classId')
    try:
        if dao.delete_hoc_sinh(student_id, class_id):
            # Cập nhật sĩ số của lớp
            class_data = db.session.query(Lop).filter(Lop.maLop == class_id).first()
            if class_data:
                class_data.siSo -= 1  # Giảm sĩ số đi 1
                db.session.commit()
            return jsonify({'message': 'Học sinh đã được xóa thành công.'}), 200
        return jsonify({'error': 'Học sinh không tồn tại trong lớp.'}), 404
    except Exception as e:
        db.session.rollback()  # Hoàn tác nếu có lỗi
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()


@app.route('/api/add_student', methods=['POST'])
def add_student():
    data = request.json
    required_fields = ['maHocSinh', 'tenLop']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Thiếu thông tin cần thiết.'}), 400


    session = db.session
    maHocSinh = data['maHocSinh']
    tenLop = data['tenLop']
    maLop=session.query(Lop).filter(Lop.tenLop == tenLop).first().maLop
    print(maHocSinh)
    print(tenLop)
    print(maLop)
    try:
        # Lấy thông tin lớp
        class_data = session.query(Lop).filter(Lop.maLop == maLop).first()
        if not class_data:
            return jsonify({'error': 'Lớp không tồn tại.'}), 404

        # Lấy năm học từ bảng HocSinhLop
        hoc_sinh_lop_data = session.query(HocSinhLop).filter(HocSinhLop.maLop == maLop).first()
        if not hoc_sinh_lop_data:
            return jsonify({'error': 'Không tìm thấy thông tin năm học cho lớp này.'}), 404

        namHoc = hoc_sinh_lop_data.namHoc  # Lấy năm học từ bản ghi đầu tiên
        # Kiểm tra xem học sinh đã có trong lớp chưa
        existing_record = session.query(HocSinhLop).filter(
            HocSinhLop.maHocSinh == maHocSinh,
            HocSinhLop.maLop == maLop,
            HocSinhLop.namHoc == namHoc
        ).first()

        if existing_record:
            return jsonify({'message': 'Học sinh đã có trong lớp.'}), 400  # Trả về thông báo nếu đã có

        # Thêm học sinh vào lớp
        dao.add_hoc_sinh_vao_lop(maHocSinh, maLop, namHoc)

        # Cập nhật sĩ số của lớp
        class_data.siSo += 1
        session.commit()

        return jsonify({'classId':maLop,'message': 'Học sinh đã được thêm vào lớp thành công.'}), 201
    except Exception as e:
        session.rollback()  # Hoàn tác nếu có lỗi
        return jsonify({'error': 'Có lỗi xảy ra khi thêm học sinh: ' + str(e)}), 500
    finally:
        session.close()


@app.route('/api/update_class_name', methods=['POST'])
def update_class_name():
    data = request.get_json()
    old_class_name = data.get('oldClassName')
    new_class_name = data.get('newClassName')

    # Tìm lớp theo tên cũ
    class_to_update = db.session.query(Lop).filter_by(tenLop=old_class_name).first()

    if class_to_update:
        # Cập nhật tên lớp
        class_to_update.tenLop = new_class_name
        db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu
        return jsonify({'class_id':class_to_update.maLop,'message': 'Tên lớp đã được cập nhật.'}), 200
    else:
        return jsonify({'message': 'Không tìm thấy lớp với tên đã cho.'}), 404

@app.route('/api/report', methods=['GET'])
def get_report():
    nam_hoc = request.args.get('namHoc')
    khoi = request.args.get('khoi')
    hoc_ky = request.args.get('hocky')
    mon_hoc = request.args.get('monhoc')

    query = db.session.query(LopMonHoc).filter_by(maMonHoc=mon_hoc).all()

    report_data = []

    for lop_mon in query:
        # Lấy thông tin lớp từ mã lớp
        lop_info = db.session.query(Lop).filter_by(maLop=lop_mon.maLop).first()
        ten_lop = lop_info.tenLop if lop_info else "Không xác định"  # Lấy tên lớp

        hoc_sinh_list = db.session.query(HocSinhLop).filter_by(maLop=lop_mon.maLop, namHoc=nam_hoc).all()
        si_so = len(hoc_sinh_list)
        count_passed = 0  # Số học sinh đạt

        for hoc_sinh in hoc_sinh_list:
            diem_hs = db.session.query(Diem).filter_by(maHocSinh=hoc_sinh.maHocSinh, maHocKy=hoc_ky,
                                                       maMonHoc=mon_hoc).all()
            # Kiểm tra xem có điểm nào rỗng không
            if not diem_hs:
                return jsonify({'error': 'Tồn tại học sinh trong ít nhất 1 lớp chưa có điểm của môn học này, không thể lập báo cáo'}), 400

            average_score = calculate_average_score(diem_hs)  # Tính điểm trung bình cho học sinh

            if average_score >= 5:
                count_passed += 1  # Tăng số học sinh đạt

        ti_le = (count_passed / si_so * 100) if si_so > 0 else 0  # Tính tỷ lệ đạt

        report_data.append({
            'stt': len(report_data) + 1,
            'lop': ten_lop,  # Gán tên lớp vào đây
            'siSo': si_so,
            'soLuongDat': count_passed,
            'tiLe': ti_le
        })

    db.session.close()
    return jsonify(report_data)

# Hàm tính điểm trung bình
def calculate_average_score(diem_list):
    total_score = 0
    total_coefficient = 0

    for diem in diem_list:
        coefficient = 0
        print(diem.loaiDiem)
        if diem.loaiDiem == LoaiDiem.PHUT_15:
            coefficient = 1
        elif diem.loaiDiem in [LoaiDiem.TIET_1, LoaiDiem.GIUA_KI]:
            coefficient = 2
        elif diem.loaiDiem == LoaiDiem.CUOI_KI:
            coefficient = 3
        # print(diem.giaTriDiem)
        total_score += diem.giaTriDiem * coefficient
        total_coefficient += coefficient
    print(total_score / total_coefficient)

    return total_score / total_coefficient if total_coefficient > 0 else 0  # Tránh chia cho 0

# # Hàm chuyển đổi đối tượng Diem sang từ điển
# def diem_to_dict(diem):
#     return {
#         'maMonHoc': diem.maMonHoc,
#         'maHocSinh': diem.maHocSinh,
#         'maHocKy': diem.maHocKy,
#         'soThuTuDiem': diem.soThuTuDiem,
#         'giaTriDiem': diem.giaTriDiem,
#         'loaiDiem': diem.loaiDiem.value  # Lưu ý: sử dụng .value để lấy giá trị chuỗi
#     }


if __name__ == '__main__':
    from App import admin
    app.run(debug=True,port=8888)
