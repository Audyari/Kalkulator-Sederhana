# 🧮 Template Project Management: Kalkulator Sederhana Python

## 📋 Project Overview
**Project Name:** Simple Calculator Python  
**Duration Estimate:** 2-4 hari  
**Difficulty:** Beginner  
**Goal:** Membuat kalkulator console sederhana dengan operasi matematika dasar

---

## 🎯 Phase 1: PROJECT SETUP & PLANNING
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 1.1 Environment Setup
- [x] **Install Python 3.7+** *(15 menit)*
  - Versi terinstall: Python 3.12.2
- [x] **Setup Code Editor** *(10 menit)*
  - Install VS Code / PyCharm / Sublime
  - Install Python extension
- [ ] **Create Project Structure** *(5 menit)*
  - Buat folder `simple-calculator`
  - Buat file `main.py`
  - Buat file `README.md`

### 1.2 Version Control Setup
- [ ] **Initialize Git Repository** *(10 menit)*
  - `git init`
  - Create `.gitignore` untuk Python
  - First commit dengan project structure
- [ ] **Create GitHub Repository** *(10 menit)*
  - Buat repo di GitHub
  - Connect local dengan remote
  - Push initial commit

**Phase 1 Total Estimate:** 1 jam

---

## 🔧 Phase 2: CORE FUNCTIONALITY
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 2.1 Basic Math Functions
- [ ] **Create Addition Function** *(15 menit)*
  ```python
  def add(a, b):
      return a + b
  ```
  - Test dengan beberapa angka
  - Print hasil untuk validasi

- [ ] **Create Subtraction Function** *(15 menit)*
  ```python
  def subtract(a, b):
      return a - b
  ```
  - Test dengan angka positif & negatif

- [ ] **Create Multiplication Function** *(15 menit)*
  ```python
  def multiply(a, b):
      return a * b
  ```
  - Test dengan decimal numbers

- [ ] **Create Division Function** *(20 menit)*
  ```python
  def divide(a, b):
      if b != 0:
          return a / b
      else:
          return "Error: Division by zero"
  ```
  - Handle division by zero case

### 2.2 Function Testing
- [ ] **Test All Math Functions** *(20 menit)*
  - Buat test cases untuk setiap function
  - Validate hasil perhitungan manual
  - Document expected vs actual results

**Phase 2 Total Estimate:** 1.5 jam

---

## 🖥️ Phase 3: USER INTERFACE
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 3.1 Menu System
- [ ] **Create Main Menu** *(30 menit)*
  - Display operation choices (1-4)
  - Show welcome message
  - Format menu dengan ASCII art (optional)

- [ ] **Implement Menu Selection** *(20 menit)*
  - Get user input untuk pilihan menu
  - Validate input (1-4 only)
  - Handle invalid selections

### 3.2 Input Handling
- [ ] **Get Numbers from User** *(25 menit)*
  - Input angka pertama
  - Input angka kedua
  - Convert string to float/int

- [ ] **Display Results** *(15 menit)*
  - Format output yang readable
  - Show calculation process
  - Display final result

### 3.3 Program Flow
- [ ] **Create Main Loop** *(20 menit)*
  - Implement "Continue?" functionality
  - Exit option
  - Clear screen between calculations

**Phase 3 Total Estimate:** 2 jam

---

## 🛡️ Phase 4: ERROR HANDLING & VALIDATION
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 4.1 Input Validation
- [ ] **Validate Numeric Input** *(30 menit)*
  - Check if input is number
  - Handle letters/special characters
  - Provide clear error messages

- [ ] **Validate Menu Choice** *(15 menit)*
  - Ensure choice is 1-4
  - Handle empty input
  - Re-prompt on invalid choice

### 4.2 Math Error Handling
- [ ] **Handle Division by Zero** *(15 menit)*
  - Proper error message
  - Allow user to retry
  - Don't crash program

- [ ] **Handle Large Numbers** *(10 menit)*
  - Test with very large numbers
  - Handle overflow cases
  - Set reasonable limits if needed

### 4.3 Exception Handling
- [ ] **Implement Try-Catch Blocks** *(20 menit)*
  - Wrap risky operations
  - Graceful error handling
  - User-friendly error messages

**Phase 4 Total Estimate:** 1.5 jam

---

## ⚡ Phase 5: ENHANCED FEATURES (Optional)
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 5.1 Additional Operations
- [ ] **Add Power/Exponent Function** *(20 menit)*
  - `a ** b` operation
  - Add to menu as option 5

- [ ] **Add Square Root Function** *(20 menit)*
  - Import math module
  - Handle negative numbers

- [ ] **Add Percentage Calculation** *(15 menit)*
  - Percentage of number
  - Percentage increase/decrease

### 5.2 Memory Features
- [ ] **Add Calculation History** *(45 menit)*
  - Store last 5 calculations
  - Display history option
  - Clear history function

- [ ] **Add Memory Storage** *(30 menit)*
  - Store current result
  - Recall stored number
  - Clear memory function

**Phase 5 Total Estimate:** 2 jam

---

## 🧪 Phase 6: TESTING & DEBUGGING
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 6.1 Functional Testing
- [ ] **Test All Math Operations** *(30 menit)*
  - Positive numbers
  - Negative numbers
  - Decimal numbers
  - Large numbers

- [ ] **Test Error Scenarios** *(20 menit)*
  - Division by zero
  - Invalid inputs
  - Empty inputs
  - Special characters

### 6.2 User Experience Testing
- [ ] **Test Program Flow** *(20 menit)*
  - Complete calculation cycles
  - Exit functionality
  - Continue functionality
  - Menu navigation

- [ ] **Get User Feedback** *(30 menit)*
  - Ask friend/colleague to test
  - Note confusing parts
  - Gather improvement suggestions

**Phase 6 Total Estimate:** 1.5 jam

---

## 📝 Phase 7: CODE QUALITY & DOCUMENTATION
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 7.1 Code Optimization
- [ ] **Add Comments** *(20 menit)*
  - Function descriptions
  - Complex logic explanations
  - Code section headers

- [ ] **Code Refactoring** *(30 menit)*
  - Remove duplicate code
  - Improve variable names
  - Organize functions logically

- [ ] **Follow Python Conventions** *(15 menit)*
  - PEP 8 style guide
  - Proper naming conventions
  - Consistent indentation

### 7.2 Documentation
- [ ] **Write README.md** *(30 menit)*
  - Project description
  - How to run
  - Features list
  - Screenshots/examples

- [ ] **Add Inline Documentation** *(15 menit)*
  - Docstrings for functions
  - Usage examples
  - Parameter descriptions

**Phase 7 Total Estimate:** 2 jam

---

## 🚀 Phase 8: DEPLOYMENT & SHARING
**Status:** ⏳ To Do | 🔄 In Progress | ✅ Done

### 8.1 Final Preparations
- [ ] **Final Testing** *(20 menit)*
  - Complete end-to-end test
  - Check all features work
  - Verify error handling

- [ ] **Code Cleanup** *(15 menit)*
  - Remove debug prints
  - Clean up test code
  - Final formatting check

### 8.2 Publishing
- [ ] **Push to GitHub** *(10 menit)*
  - Final commit dengan message yang jelas
  - Push semua changes
  - Create release tag v1.0

- [ ] **Create Portfolio Entry** *(30 menit)*
  - Add to personal portfolio
  - Write project description
  - Include lessons learned

- [ ] **Share Project** *(15 menit)*
  - Post di LinkedIn (optional)
  - Share dengan teman/komunitas
  - Get feedback untuk project selanjutnya

**Phase 8 Total Estimate:** 1.5 jam

---

## 📊 PROJECT SUMMARY

**Total Estimated Time:** 12-15 jam  
**Timeline:** 2-4 hari (3-4 jam per hari)  
**Skill Level:** Beginner  
**Technologies:** Python, Git, GitHub  

### Key Learning Outcomes:
- ✅ Python functions & basic syntax
- ✅ User input handling
- ✅ Error handling & validation
- ✅ Code organization & documentation
- ✅ Version control dengan Git
- ✅ Project management & task breaking

### Next Project Suggestions:
1. **Guess the Number Game** - Add random numbers & loops
2. **To-Do List App** - File handling & data persistence
3. **Weather App** - API integration & JSON handling

---

## 🛠️ Tools Integration

### For Trello:
- Buat board baru "Simple Calculator Python"
- 3 Lists: "To Do", "In Progress", "Done"
- Setiap Phase jadi Card
- Sub-tasks jadi Checklist dalam card

### For Notion:
- Template ini bisa langsung di-copy ke Notion
- Gunakan database untuk tracking progress
- Add deadline untuk setiap phase

### For GitHub Projects:
- Convert setiap sub-task jadi GitHub Issue
- Gunakan labels: "setup", "feature", "testing", "docs"
- Link issues ke pull requests

---

**Happy Coding! 🎉**