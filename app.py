# Add these imports to your existing app.py (at the top with other imports)

# Import the new licensing module
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

# Add this to your existing system status section (around line where you check other systems)

def check_all_system_status():
    """Check status of all integrated systems"""
    systems_status = {}
    
    # Foundation system status (your existing code)
    try:
        foundation_status = get_foundation_system_status()
        systems_status['foundation'] = foundation_status
    except:
        systems_status['foundation'] = {'available': False}
    
    # Employee system status (your existing code)
    try:
        employee_status = get_employee_system_status()
        systems_status['employee'] = employee_status
    except:
        systems_status['employee'] = {'available': False}
    
    # Payroll system status (your existing code)
    try:
        payroll_status = get_payroll_system_status()
        systems_status['payroll'] = payroll_status
    except:
        systems_status['payroll'] = {'available': False}
    
    # NEW: Licensing system status
    if LICENSING_AVAILABLE:
        try:
            licensing_status = get_licensing_system_status()
            systems_status['licensing'] = licensing_status
        except:
            systems_status['licensing'] = {'available': False}
    else:
        systems_status['licensing'] = {'available': False}
    
    return systems_status

# Update your main page navigation to include the new licensing button
# Add this to your main page button section (where you have Foundation, Employee, Payroll buttons)

def render_main_page():
    """Render the main navigation page with all systems"""
    
    # Your existing header code...
    
    # System status overview (your existing code)
    systems_status = check_all_system_status()
    
    # Enhanced status display with licensing
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
        # NEW: Licensing system status
        licensing_available = systems_status.get('licensing', {}).get('available', False)
        status_icon = "🟢" if licensing_available else "🔴"
        st.metric("Licensing System", f"{status_icon} {'Online' if licensing_available else 'Offline'}")
    
    st.markdown("---")
    
    # Navigation buttons section
    st.markdown("### 🚀 Choose Your Migration Tool")
    
    # Row 1: Core Data Management Systems (your existing buttons)
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
    
    # Row 2: Enterprise Management (NEW)
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
        # Placeholder for future enterprise features
        if st.button("📊 Analytics Dashboard", 
                     key="btn_analytics", 
                     use_container_width=True, 
                     disabled=True,  # Not implemented yet
                     type="secondary"):
            st.info("Coming soon! Advanced cross-system analytics.")
        st.caption("Cross-System Analytics • KPIs • Reports")
    
    with col3:
        # Placeholder for future enterprise features
        if st.button("⚙️ System Administration", 
                     key="btn_admin", 
                     use_container_width=True, 
                     disabled=True,  # Not implemented yet
                     type="secondary"):
            st.info("Coming soon! Centralized system administration.")
        st.caption("User Management • System Config • Audit Logs")
    
    # License status warning (if applicable)
    if licensing_available:
        licensing_status = systems_status.get('licensing', {})
        if not licensing_status.get('license_valid', True):
            st.error("⚠️ **License Issue:** Your license has expired or is invalid. Please contact support.")
        elif licensing_status.get('credits_remaining', 0) < 500:
            st.warning("⚠️ **Low Credits:** You're running low on processing credits. Consider upgrading your plan.")

# Add this to your main navigation logic (in your existing if/elif statements)

# Your existing navigation logic...
elif st.session_state.demo_page == "foundation_data_view":
    # Your existing foundation code...

elif st.session_state.demo_page == "employee_data_management":
    # Your existing employee code...

elif st.session_state.demo_page == "payroll_data_tool":
    # Your existing payroll code...

# NEW: Add this section for licensing management
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

# Optional: Add a footer with licensing info to your main page
def render_app_footer():
    """Render app footer with licensing information"""
    if LICENSING_AVAILABLE:
        try:
            licensing_status = get_licensing_system_status()
            
            st.markdown("---")
            footer_col1, footer_col2, footer_col3 = st.columns(3)
            
            with footer_col1:
                st.caption(f"License: {licensing_status.get('subscription_tier', 'Unknown')}")
            
            with footer_col2:
                credits_remaining = licensing_status.get('credits_remaining', 0)
                st.caption(f"Credits Remaining: {credits_remaining:,}")
            
            with footer_col3:
                users_active = licensing_status.get('users_active', 0)
                st.caption(f"Active Users: {users_active}")
        
        except:
            st.caption("SAP Migration Suite © 2024")
    else:
        st.caption("SAP Migration Suite © 2024")

# Call this at the bottom of your main function
# render_app_footer()
