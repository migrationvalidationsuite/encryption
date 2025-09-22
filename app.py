import streamlit as st
import pandas as pd

# Configure Streamlit page
st.set_page_config(
    page_title="SAP Migration Suite",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import the licensing module
try:
    from packaging_licensing_module import (
        render_licensing_dashboard, 
        get_licensing_system_status,
        init_licensing_state
    )
    LICENSING_AVAILABLE = True
except ImportError as e:
    LICENSING_AVAILABLE = False
    print(f"Licensing module not available: {e}")

# Initialize session state
if 'demo_page' not in st.session_state:
    st.session_state.demo_page = "main"

def show_header():
    """Display main header with branding"""
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3d59 0%, #2e5984 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; text-align: center;">🏢 SAP Migration Suite</h1>
        <p style="color: #e0e8f0; text-align: center; margin: 0.5rem 0 0 0;">
            Complete Enterprise Migration Platform with Licensing & Packaging
        </p>
    </div>
    """, unsafe_allow_html=True)

def get_system_status():
    """Get status of all systems"""
    # For demo purposes, we'll simulate system availability
    # In a real app, these would check actual system connectivity
    return {
        'foundation': {'available': True},
        'employee': {'available': True},
        'payroll': {'available': True},
        'licensing': {'available': LICENSING_AVAILABLE}
    }

def render_main_page():
    """Render the main navigation page"""
    show_header()
    
    # System status overview
    systems_status = get_system_status()
    
    st.markdown("### 📊 System Status")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        foundation_available = systems_status.get('foundation', {}).get('available', False)
        status_icon = "🟢" if foundation_available else "🔴"
        st.metric("Foundation System", f"{status_icon} {'Online' if foundation_available else 'Offline'}")
    
    with col2:
        employee_available = systems_status.get('employee', {}).get('available', False)
        status_icon = "🟢" if employee_available else "🔴"
        st.metric("Employee System", f"{status_icon} {'Online' if employee_available else 'Offline'}")
    
    with col3:
        payroll_available = systems_status.get('payroll', {}).get('available', False)
        status_icon = "🟢" if payroll_available else "🔴"
        st.metric("Payroll System", f"{status_icon} {'Online' if payroll_available else 'Offline'}")
    
    with col4:
        licensing_available = systems_status.get('licensing', {}).get('available', False)
        status_icon = "🟢" if licensing_available else "🔴"
        st.metric("Licensing System", f"{status_icon} {'Online' if licensing_available else 'Offline'}")
    
    st.markdown("---")
    
    # Navigation buttons section
    st.markdown("### 🚀 Choose Your Migration Tool")
    
    # Row 1: Core Data Management Systems
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏢 Foundation Data", 
                     key="btn_foundation", 
                     use_container_width=True, 
                     disabled=not foundation_available):
            st.session_state.demo_page = "foundation_data_view"
            st.rerun()
        st.caption("Organizational Hierarchy • HRP1000/HRP1001")
    
    with col2:
        if st.button("👥 Employee Data", 
                     key="btn_employee", 
                     use_container_width=True, 
                     disabled=not employee_available):
            st.session_state.demo_page = "employee_data_management"
            st.rerun()
        st.caption("Personnel Information • PA0001/PA0002/PA0006/PA0105")
    
    with col3:
        if st.button("💰 Payroll Data", 
                     key="btn_payroll", 
                     use_container_width=True, 
                     disabled=not payroll_available):
            st.session_state.demo_page = "payroll_data_tool"
            st.rerun()
        st.caption("Compensation Processing • PA0008/PA0014")
    
    # Row 2: Enterprise Management
    st.markdown("### 🏢 Enterprise Management")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔐 Licensing & Subscription", 
                     key="btn_licensing", 
                     use_container_width=True, 
                     disabled=not licensing_available,
                     type="secondary"):
            st.session_state.demo_page = "licensing_management"
            st.rerun()
        st.caption("License Management • Billing • Packaging")
    
    with col2:
        if st.button("📊 Analytics Dashboard", 
                     key="btn_analytics", 
                     use_container_width=True, 
                     disabled=True,
                     type="secondary"):
            st.info("Coming soon! Advanced cross-system analytics.")
        st.caption("Cross-System Analytics • KPIs • Reports")
    
    with col3:
        if st.button("⚙️ System Administration", 
                     key="btn_admin", 
                     use_container_width=True, 
                     disabled=True,
                     type="secondary"):
            st.info("Coming soon! Centralized system administration.")
        st.caption("User Management • System Config • Audit Logs")
    
    # License status warnings (if licensing is available)
    if licensing_available and LICENSING_AVAILABLE:
        try:
            licensing_status = get_licensing_system_status()
            if not licensing_status.get('license_valid', True):
                st.error("⚠️ **License Issue:** Your license has expired or is invalid. Please contact support.")
            elif licensing_status.get('credits_remaining', 0) < 500:
                st.warning("⚠️ **Low Credits:** You're running low on processing credits. Consider upgrading your plan.")
        except Exception:
            pass  # Silently handle any licensing status errors
    
    # Demo information
    st.markdown("---")
    st.markdown("### 💡 Demo Information")
    st.info("""
    **Welcome to the SAP Migration Suite Demo!**
    
    This demonstration showcases our complete enterprise-grade SAP migration platform including:
    - 🏢 **Foundation Data Processing** - Organizational hierarchy migration (HRP1000/HRP1001)
    - 👥 **Employee Data Management** - Personnel record processing (PA0001/PA0002/PA0006/PA0105)  
    - 💰 **Payroll Data Processing** - Compensation migration (PA0008/PA0014)
    - 🔐 **Enterprise Licensing** - Subscription management, packaging, and billing
    
    Click any button above to explore the different modules!
    """)

def render_foundation_demo():
    """Demo placeholder for Foundation Data system"""
    st.header("🏢 Foundation Data Management")
    st.info("This would be your Foundation Data Management system for organizational hierarchy processing.")
    st.markdown("**Features would include:**")
    st.write("• HRP1000 & HRP1001 file processing")
    st.write("• Organizational structure validation")
    st.write("• Hierarchy mapping and transformation")
    st.write("• Data quality checks and reporting")

def render_employee_demo():
    """Demo placeholder for Employee Data system"""
    st.header("👥 Employee Data Management")
    st.info("This would be your Employee Data Management system for personnel record processing.")
    st.markdown("**Features would include:**")
    st.write("• PA0001, PA0002, PA0006, PA0105 file processing")
    st.write("• Employee record validation and cleansing")
    st.write("• Data transformation and mapping")
    st.write("• Statistical analysis and reporting")

def render_payroll_demo():
    """Demo placeholder for Payroll Data system"""
    st.header("💰 Payroll Data Management")
    st.info("This would be your Payroll Data Management system for compensation processing.")
    st.markdown("**Features would include:**")
    st.write("• PA0008 & PA0014 file processing")
    st.write("• Wage type analysis and validation")
    st.write("• Payment verification and reconciliation")
    st.write("• Payroll insights and analytics")

def render_app_footer():
    """Render app footer with system information"""
    st.markdown("---")
    
    if LICENSING_AVAILABLE:
        try:
            licensing_status = get_licensing_system_status()
            
            footer_col1, footer_col2, footer_col3, footer_col4 = st.columns(4)
            
            with footer_col1:
                st.caption(f"**License:** {licensing_status.get('subscription_tier', 'Demo')}")
            
            with footer_col2:
                credits_remaining = licensing_status.get('credits_remaining', 0)
                st.caption(f"**Credits:** {credits_remaining:,}")
            
            with footer_col3:
                users_active = licensing_status.get('users_active', 0)
                st.caption(f"**Users:** {users_active}")
            
            with footer_col4:
                st.caption("**Status:** Demo Mode")
        except Exception:
            st.caption("SAP Migration Suite © 2024 • Demo Version")
    else:
        st.caption("SAP Migration Suite © 2024 • Demo Version")

def main():
    """Main application function"""
    
    # Main navigation logic
    if st.session_state.demo_page == "main":
        render_main_page()
    
    elif st.session_state.demo_page == "foundation_data_view":
        if st.button("← Back to Main", key="back_from_foundation"):
            st.session_state.demo_page = "main"
            st.rerun()
        render_foundation_demo()
    
    elif st.session_state.demo_page == "employee_data_management":
        if st.button("← Back to Main", key="back_from_employee"):
            st.session_state.demo_page = "main"
            st.rerun()
        render_employee_demo()
    
    elif st.session_state.demo_page == "payroll_data_tool":
        if st.button("← Back to Main", key="back_from_payroll"):
            st.session_state.demo_page = "main"
            st.rerun()
        render_payroll_demo()
    
    elif st.session_state.demo_page == "licensing_management":
        if st.button("← Back to Main", key="back_from_licensing"):
            st.session_state.demo_page = "main"
            st.rerun()
        
        if LICENSING_AVAILABLE:
            render_licensing_dashboard()
        else:
            st.error("❌ Licensing system is not available")
            st.info("**Troubleshooting:**")
            st.write("1. Ensure `packaging_licensing_module.py` is in your project directory")
            st.write("2. Check that all required dependencies are installed")
            st.write("3. Verify file permissions and import paths")
            st.write("4. Check for any Python syntax errors in the licensing module")
    
    # Always show footer
    render_app_footer()

if __name__ == "__main__":
    main()
