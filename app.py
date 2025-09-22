import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Configure Streamlit page
st.set_page_config(
    page_title="Licensing & Subscription Demo",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "main"

if 'licensing_state' not in st.session_state:
    st.session_state.licensing_state = {
        'license_type': 'Enterprise',
        'license_valid': True,
        'license_expiry': '2025-12-31',
        'organization': 'Global Corp Inc.',
        'max_users': 25,
        'current_users': 15,
        'monthly_credits': 10000,
        'used_credits': 8500,
        'subscription_tier': 'Enterprise Plus',
        'monthly_cost': 2450.00,
        'auto_renewal': True,
        'features_enabled': [
            'Foundation Data Processing',
            'Employee Data Management', 
            'Payroll Data Processing',
            'Advanced Analytics',
            'Custom Reports',
            'API Access',
            'Priority Support',
            'Audit Trail',
            'Encrypted Packaging',
            'Multi-tenant Support'
        ]
    }

def show_main_page():
    """Show the main landing page"""
    
    # Header
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3d59 0%, #2e5984 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; text-align: center;">🔐 Licensing & Subscription Management</h1>
        <p style="color: #e0e8f0; text-align: center; margin: 0.5rem 0 0 0;">
            Enterprise-grade licensing, packaging, and subscription management platform
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick overview cards
    licensing_state = st.session_state.licensing_state
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "License Status", 
            "✅ Active" if licensing_state['license_valid'] else "❌ Expired",
            help=f"Valid until {licensing_state['license_expiry']}"
        )
    
    with col2:
        st.metric(
            "Subscription Tier", 
            licensing_state['subscription_tier'],
            help="Current subscription level"
        )
    
    with col3:
        usage_pct = (licensing_state['used_credits'] / licensing_state['monthly_credits']) * 100
        st.metric(
            "Credit Usage", 
            f"{usage_pct:.1f}%",
            f"{licensing_state['used_credits']:,}/{licensing_state['monthly_credits']:,}"
        )
    
    with col4:
        st.metric(
            "Active Users", 
            f"{licensing_state['current_users']}/{licensing_state['max_users']}",
            help="Current vs maximum licensed users"
        )
    
    st.markdown("---")
    
    # Main navigation buttons
    st.markdown("### Choose Management Area")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 License Details", use_container_width=True, type="primary"):
            st.session_state.current_page = "license_details"
            st.rerun()
        st.caption("View license information, features, and expiry details")
        
        if st.button("📦 Packaging Tools", use_container_width=True):
            st.session_state.current_page = "packaging"
            st.rerun()
        st.caption("Generate packages, configure security, and deployment settings")
    
    with col2:
        if st.button("💳 Billing & Usage", use_container_width=True):
            st.session_state.current_page = "billing"
            st.rerun()
        st.caption("View billing breakdown, usage analytics, and cost trends")
        
        if st.button("⚙️ Configuration", use_container_width=True):
            st.session_state.current_page = "configuration"
            st.rerun()
        st.caption("Manage subscriptions, users, and system settings")
    
    # Demo information
    st.markdown("---")
    st.markdown("### Demo Overview")
    st.info("""
    **Welcome to the Licensing & Subscription Management Demo!**
    
    This platform provides complete enterprise licensing capabilities including:
    - **License Management** - Track validity, features, and user limits
    - **Billing Analytics** - Monitor costs, usage trends, and payment processing
    - **Package Generation** - Create secure, deployable software packages
    - **Subscription Control** - Manage plans, upgrades, and renewals
    
    Click any button above to explore the different management areas.
    """)

def show_license_details():
    """Show detailed license information"""
    licensing_state = st.session_state.licensing_state
    
    # Back button
    if st.button("← Back to Main", key="back_license"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("📋 License Details")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Basic Information")
        st.write(f"**License Type:** {licensing_state['license_type']}")
        st.write(f"**Organization:** {licensing_state['organization']}")
        st.write(f"**Valid Until:** {licensing_state['license_expiry']}")
        st.write(f"**Max Users:** {licensing_state['max_users']}")
        st.write(f"**Monthly Credits:** {licensing_state['monthly_credits']:,}")
        
        # License health check
        expiry_date = datetime.strptime(licensing_state['license_expiry'], '%Y-%m-%d')
        days_remaining = (expiry_date - datetime.now()).days
        
        if days_remaining > 30:
            st.success(f"✅ License expires in {days_remaining} days")
        elif days_remaining > 0:
            st.warning(f"⚠️ License expires in {days_remaining} days")
        else:
            st.error("❌ License has expired")
    
    with col2:
        st.subheader("Enabled Features")
        
        # Group features by category
        feature_categories = {
            "Core Processing": [
                "Foundation Data Processing",
                "Employee Data Management", 
                "Payroll Data Processing"
            ],
            "Advanced Analytics": [
                "Advanced Analytics",
                "Custom Reports",
                "API Access"
            ],
            "Enterprise Features": [
                "Priority Support",
                "Audit Trail",
                "Encrypted Packaging",
                "Multi-tenant Support"
            ]
        }
        
        for category, features in feature_categories.items():
            st.markdown(f"**{category}:**")
            for feature in features:
                if feature in licensing_state['features_enabled']:
                    st.write(f"✅ {feature}")
                else:
                    st.write(f"❌ {feature} (Not included)")
            st.write("")

def show_billing_usage():
    """Show billing and usage analytics"""
    licensing_state = st.session_state.licensing_state
    
    # Back button
    if st.button("← Back to Main", key="back_billing"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("💳 Billing & Usage Analytics")
    
    # Current billing overview
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Billing breakdown chart
        billing_data = {
            'Service': ['Base Subscription', 'Processing Credits', 'Premium Support', 'API Calls', 'Storage', 'Additional Users'],
            'Cost': [1200, 850, 300, 75, 25, 150],
            'Usage': ['100%', '85%', '100%', '45%', '12%', '60%']
        }
        
        df_billing = pd.DataFrame(billing_data)
        
        fig = px.pie(
            df_billing, 
            values='Cost', 
            names='Service',
            title="Monthly Cost Breakdown",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Current Bill Summary")
        st.metric("Monthly Total", f"${licensing_state['monthly_cost']:,.2f}")
        st.metric("Next Bill Date", "Oct 1, 2024")
        st.metric("Payment Method", "•••• 4567")
        
        # Usage warnings
        usage_pct = (licensing_state['used_credits'] / licensing_state['monthly_credits']) * 100
        if usage_pct > 90:
            st.error("⚠️ Credit limit almost reached!")
        elif usage_pct > 75:
            st.warning("⚠️ High credit usage detected")
        
        st.dataframe(df_billing[['Service', 'Cost']], use_container_width=True)
    
    # Usage trends
    st.subheader("Usage Trends")
    
    # Generate sample usage data
    dates = pd.date_range(start='2024-07-01', end='2024-09-22', freq='D')
    daily_usage = []
    
    for i, date in enumerate(dates):
        base_usage = 200 + (i % 30) * 15
        weekend_factor = 0.6 if date.weekday() >= 5 else 1.0
        seasonal_factor = 1 + 0.3 * (i / len(dates))
        usage = int(base_usage * weekend_factor * seasonal_factor)
        daily_usage.append(usage)
    
    df_usage = pd.DataFrame({
        'Date': dates,
        'Credits Used': daily_usage,
        'Cumulative': pd.Series(daily_usage).cumsum()
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.line(df_usage, x='Date', y='Credits Used', title="Daily Credit Usage")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.line(df_usage, x='Date', y='Cumulative', title="Cumulative Monthly Usage")
        st.plotly_chart(fig, use_container_width=True)

def show_packaging_tools():
    """Show packaging and deployment tools"""
    licensing_state = st.session_state.licensing_state
    
    # Back button
    if st.button("← Back to Main", key="back_packaging"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("📦 Packaging & Deployment Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Package Configuration")
        
        package_name = st.text_input("Package Name", value="SAP_Migration_Suite_v2.1")
        
        include_foundation = st.checkbox("Include Foundation Module", value=True)
        include_employee = st.checkbox("Include Employee Module", value=True)
        include_payroll = st.checkbox("Include Payroll Module", value=True)
        
        st.subheader("Security Settings")
        encrypt_package = st.checkbox("Encrypt Package", value=True)
        digital_signature = st.checkbox("Add Digital Signature", value=True)
        audit_trail = st.checkbox("Include Audit Trail", value=True)
        
        encryption_level = st.selectbox("Encryption Level", ["AES-256", "AES-128", "RSA-2048"], index=0)
    
    with col2:
        st.subheader("Deployment Settings")
        
        deployment_target = st.selectbox(
            "Deployment Target",
            ["Cloud (Auto-Update)", "On-Premise", "Hybrid", "Custom"],
            help="Choose deployment environment"
        )
        
        auto_update = st.checkbox("Enable Auto-Updates", value=True)
        multi_tenant = st.checkbox("Multi-Tenant Support", value=True)
        api_enabled = st.checkbox("Enable API Access", value=True)
        
        st.subheader("Package Contents")
        
        # Calculate package size estimates
        base_size = 50
        foundation_size = 25 if include_foundation else 0
        employee_size = 30 if include_employee else 0
        payroll_size = 20 if include_payroll else 0
        total_size = base_size + foundation_size + employee_size + payroll_size
        
        st.write(f"**Estimated Package Size:** {total_size} MB")
        st.write(f"**Components:** {sum([include_foundation, include_employee, include_payroll])} modules")
        st.write(f"**Security Level:** {'High' if encrypt_package else 'Standard'}")
    
    st.markdown("---")
    
    # Package generation buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎁 Generate Package", type="primary", use_container_width=True):
            generate_demo_package(package_name, include_foundation, include_employee, include_payroll)
    
    with col2:
        if st.button("📋 Generate Manifest", use_container_width=True):
            generate_package_manifest(package_name, licensing_state)
    
    with col3:
        if st.button("🔍 Validate Package", use_container_width=True):
            validate_package_integrity()

def show_configuration():
    """Show configuration and subscription management"""
    licensing_state = st.session_state.licensing_state
    
    # Back button
    if st.button("← Back to Main", key="back_config"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("⚙️ Configuration & Subscription Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Subscription Plans")
        
        plans = {
            'Starter': {'price': 500, 'credits': 2500, 'users': 5},
            'Professional': {'price': 1200, 'credits': 6000, 'users': 15},
            'Enterprise': {'price': 2450, 'credits': 10000, 'users': 25},
            'Enterprise Plus': {'price': 4500, 'credits': 25000, 'users': 'Unlimited'}
        }
        
        current_plan = licensing_state['subscription_tier']
        
        for plan_name, details in plans.items():
            is_current = plan_name == current_plan
            status = "✅ Current" if is_current else "Available"
            
            with st.expander(f"{plan_name} - ${details['price']}/month ({status})"):
                st.write(f"**Monthly Credits:** {details['credits']:,}")
                st.write(f"**Max Users:** {details['users']}")
                
                if plan_name == 'Starter':
                    st.write("**Features:** Basic migration tools, email support")
                elif plan_name == 'Professional':
                    st.write("**Features:** Advanced analytics, priority support, API access")
                elif plan_name == 'Enterprise':
                    st.write("**Features:** All features, 24/7 support, custom integrations")
                else:
                    st.write("**Features:** White label, on-premise, dedicated support")
                
                if not is_current:
                    if st.button(f"Upgrade to {plan_name}", key=f"upgrade_{plan_name}"):
                        st.success(f"Upgrade request submitted for {plan_name}")
    
    with col2:
        st.subheader("Account Settings")
        
        auto_renewal = st.checkbox("Auto-Renewal Enabled", value=licensing_state['auto_renewal'])
        
        st.subheader("Notification Preferences")
        usage_alerts = st.checkbox("Usage threshold alerts", value=True)
        billing_reminders = st.checkbox("Billing reminders", value=True)
        security_updates = st.checkbox("Security update notifications", value=True)
        
        st.subheader("Quick Actions")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("💳 Update Payment", use_container_width=True):
                st.info("Redirecting to secure payment portal...")
            
            if st.button("📄 Download Invoice", use_container_width=True):
                st.info("Generating invoice PDF...")
        
        with col_b:
            if st.button("👥 Manage Users", use_container_width=True):
                st.info("Opening user management panel...")
            
            if st.button("📞 Contact Support", use_container_width=True):
                st.info("Support ticket created. Response within 4 hours.")

def generate_demo_package(package_name, include_foundation, include_employee, include_payroll):
    """Generate a demo package"""
    with st.spinner("Generating package..."):
        import time
        time.sleep(2)
        
        package_contents = {
            "package_name": package_name,
            "version": "2.1.0",
            "generated_at": datetime.now().isoformat(),
            "components": {
                "foundation_module": include_foundation,
                "employee_module": include_employee,
                "payroll_module": include_payroll
            },
            "security": {
                "encrypted": True,
                "signature": "SHA256:abc123...",
                "encryption_level": "AES-256"
            },
            "license": {
                "type": "Enterprise",
                "valid_until": "2025-12-31",
                "organization": "Global Corp Inc."
            }
        }
        
        package_json = json.dumps(package_contents, indent=2)
        
        st.success("✅ Package generated successfully!")
        
        st.download_button(
            label="📥 Download Package Manifest",
            data=package_json,
            file_name=f"{package_name}_manifest.json",
            mime="application/json"
        )

def generate_package_manifest(package_name, licensing_state):
    """Generate package manifest"""
    manifest = {
        "package_info": {
            "name": package_name,
            "version": "2.1.0",
            "build_date": datetime.now().isoformat(),
            "license_type": licensing_state['license_type']
        },
        "system_requirements": {
            "python_version": ">=3.8",
            "memory": "4GB RAM minimum",
            "storage": "500MB available space",
            "dependencies": ["streamlit>=1.28.0", "pandas>=1.5.0", "plotly>=5.0.0"]
        },
        "features": licensing_state['features_enabled'],
        "checksum": "sha256:demo_checksum_value"
    }
    
    manifest_json = json.dumps(manifest, indent=2)
    
    st.success("✅ Manifest generated!")
    st.download_button(
        label="📥 Download Manifest",
        data=manifest_json,
        file_name=f"{package_name}_manifest.json",
        mime="application/json"
    )

def validate_package_integrity():
    """Validate package integrity"""
    with st.spinner("Validating package integrity..."):
        import time
        time.sleep(1.5)
        
        validation_results = {
            "Digital Signature": "✅ Valid",
            "Encryption": "✅ AES-256 confirmed", 
            "Dependencies": "✅ All satisfied",
            "License": "✅ Valid until 2025-12-31",
            "Checksum": "✅ Verified",
            "Module Integrity": "✅ All modules intact"
        }
        
        st.success("✅ Package validation completed!")
        
        for check, result in validation_results.items():
            st.write(f"**{check}:** {result}")

def main():
    """Main application function"""
    
    # Navigation logic
    if st.session_state.current_page == "main":
        show_main_page()
    elif st.session_state.current_page == "license_details":
        show_license_details()
    elif st.session_state.current_page == "billing":
        show_billing_usage()
    elif st.session_state.current_page == "packaging":
        show_packaging_tools()
    elif st.session_state.current_page == "configuration":
        show_configuration()

if __name__ == "__main__":
    main()
