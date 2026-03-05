from sqlalchemy import Boolean, Column, Integer, String, Date, Text, TIMESTAMP, ForeignKey , DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base


# =====================================================
# MAIN EMPLOYEE TABLE
# =====================================================
class EmployeeAuth(Base):
    __tablename__ = "employee_auth"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employee_joining.id"), unique=True)

    email = Column(String(100), unique=True, nullable=False)
    otp = Column(String(6))
    otp_expiry = Column(DateTime)
    is_verified = Column(Boolean, default=False)
    password = Column(String(255))

    employee = relationship("EmployeeJoining")
    __tablename__ = "employee_auth"

    id = Column(Integer, primary_key=True)
    
    employee_id = Column(Integer, ForeignKey("employee_joining.id"), unique=True)
    
    email = Column(String(100), unique=True)
    otp = Column(String(6))
    otp_expiry = Column(DateTime)
    is_verified = Column(Boolean, default=False)
    password = Column(String(255))

    employee = relationship("EmployeeJoining")

class EmployeeJoining(Base):
    __tablename__ = "employee_joining"

    id = Column(Integer, primary_key=True, index=True)

    employee_code = Column(String(50), unique=True)

    # ================= BASIC DETAILS =================
    name = Column(String(100), nullable=False)
    dob = Column(Date)
    gender = Column(String(20))
    phone = Column(String(15))
    email = Column(String(100), unique=True, nullable=False)
    doj = Column(Date)

    father_name = Column(String(100))
    mother_name = Column(String(100))
    department = Column(String(100))
    designation = Column(String(100))
    blood_group = Column(String(10))
    marital_status = Column(String(20))
    spouse_name = Column(String(100))
    aadhar_number = Column(String(20), unique=True)
    pan_number = Column(String(20), unique=True)
    permanent_address = Column(Text)
    present_address = Column(Text)
    
    # ================= EMERGENCY CONTACT =================
    
    emergency_name = Column(String(100))
    emergency_relation = Column(String(50))
    emergency_phone = Column(String(10))

    # ================= EDUCATION =================
    qualification10 = Column(String(150))
    year10 = Column(String(10))
    percent10 = Column(String(10))

    qualification12 = Column(String(150))
    year12 = Column(String(10))
    percent12 = Column(String(10))

    ug_degree = Column(String(150))
    ug_college = Column(String(150))
    ug_year = Column(String(10))
    ug_percent = Column(String(10))

    pg_degree = Column(String(150))
    pg_college = Column(String(150))
    pg_year = Column(String(10))
    pg_percent = Column(String(10))

    # ================= EXPERIENCE SUMMARY =================
    total_exp_years = Column(String(5))
    total_exp_months = Column(String(5))

    career_break = Column(String(10))  # yes / no
    career_break_duration = Column(String(50))
    career_break_reason = Column(Text)

    # ================= ESI / PF =================
    esi_applicable = Column(String(10))
    uan_number = Column(String(50))
    pf_number = Column(String(50))
    esi_number = Column(String(50))

    # ================= BANK DETAILS =================
    account_holder_name = Column(String(100))
    bank_name = Column(String(100))
    account_number = Column(String(30))
    ifsc_code = Column(String(20))
    branch_name = Column(String(100))

    status = Column(String(20), default="Active")
    
    
    resume = Column(String(255))
    sslc = Column(String(255))
    hsc = Column(String(255))
    aadharSelf = Column(String(255))
    photo = Column(String(255))
    aadharFather = Column(String(255))
    aadharMother = Column(String(255))
    panSelf = Column(String(255))
    bankPassbookPhoto = Column(String(255))
    
    created_at = Column(TIMESTAMP, server_default=func.now())

    # ================= RELATIONSHIPS =================
    trainings = relationship("Training", back_populates="employee", cascade="all, delete")
    employments = relationship("Employment", back_populates="employee", cascade="all, delete")
    dependents = relationship("Dependent", back_populates="employee", cascade="all, delete")

# =====================================================
# TRAINING TABLE
# =====================================================

class Training(Base):
    __tablename__ = "employee_trainings"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee_joining.id", ondelete="CASCADE"))

    training_name = Column(String(200))
    institute = Column(String(200))
    duration = Column(String(100))
    year = Column(String(20))
    remarks = Column(Text)

    employee = relationship("EmployeeJoining", back_populates="trainings")


# =====================================================
# EMPLOYMENT TABLE
# =====================================================

class Employment(Base):
    __tablename__ = "employee_employment"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee_joining.id", ondelete="CASCADE"))

    organization = Column(String(200))
    designation = Column(String(100))
    period = Column(String(100))
    salary = Column(String(100))
    nature = Column(String(200))
    reason = Column(Text)

    employee = relationship("EmployeeJoining", back_populates="employments")
    
    

class Dependent(Base):
    __tablename__ = "dependents"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employee_joining.id"))

    name = Column(String(100))
    dob = Column(Date)
    relation = Column(String(50))

    aadhar_number = Column(String(20))
    pan_number = Column(String(20))

    aadhar_photo = Column(String(255))
    pan_photo = Column(String(255))
    photo = Column(String(255))

    employee = relationship("EmployeeJoining", back_populates="dependents")