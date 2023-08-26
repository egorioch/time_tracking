from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, Date, Time
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    full_name = Column(String(255), index=True)
    department = Column(String(255), index=True)
    role = Column(String(255), index=True)
    img_path = Column(String(255), index=True)


class TimeTracking(Base):
    __tablename__ = "time_tracking"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employee.id"), index=True)
    employee = relationship("Employee", back_populates="time_trackings")  # Связь с Employee
    date = Column(Date, index=True)
    clock_in = Column(Time(timezone=False))
    clock_out = Column(Time(timezone=False))
    absence_reason = Column(Text)
    total_time = Column(Time(timezone=False))



