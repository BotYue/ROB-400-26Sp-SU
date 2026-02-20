import numpy as np

# Settings
# Link lengths: 0.8, 1, 1
L = {1: 0.8, 2: 1.0, 3: 1.0}

# Initial theta: 
theta = {
    1: np.deg2rad(0.0), 
    2: np.deg2rad(10.0), 
    3: np.deg2rad(-10.0)
}

# Desired pose 
target = np.array([1.3, 0.6, 0.0, 0.0, 0.0, np.deg2rad(40.0)])
# Hyperparameters
lam, K, dt, N = 0.1, 1.0, 0.1, 50 

def get_pose(q):
    # p1, p2, p3 are absolute angles from the base
    p1 = q[1]
    p2 = q[1] + q[2]
    p3 = q[1] + q[2] + q[3]
    
    x = L[1]*np.cos(p1) + L[2]*np.cos(p2) + L[3]*np.cos(p3)
    y = L[1]*np.sin(p1) + L[2]*np.sin(p2) + L[3]*np.sin(p3)
    return np.array([x, y, 0, 0, 0, p3])

def get_jacobian(q):
    p1 = q[1]
    p2 = q[1] + q[2]
    p3 = q[1] + q[2] + q[3]
    
    s = [0, np.sin(p1), np.sin(p2), np.sin(p3)]
    c = [0, np.cos(p1), np.cos(p2), np.cos(p3)]
    
    J = np.zeros((6, 3))
    # Rows for X and Y velocity
    J[0, :] = [-(L[1]*s[1]+L[2]*s[2]+L[3]*s[3]), -(L[2]*s[2]+L[3]*s[3]), -L[3]*s[3]]
    J[1, :] = [ (L[1]*c[1]+L[2]*c[2]+L[3]*c[3]),  (L[2]*c[2]+L[3]*c[3]),  L[3]*c[3]]
    # Row for Yaw (angular velocity around Z)
    J[5, :] = [1, 1, 1]
    return J

print("-" * 30)
print("COPY THE LINES BELOW INTO LUA:")
print("-" * 30)
print("local qdotUpdates = {")


for i in range(N):
    curr = get_pose(theta)
    err = target - curr
    err[5] = (err[5] + np.pi) % (2 * np.pi) - np.pi # Yaw wrap
    
    J = get_jacobian(theta)
    # DLS solve
    qdot = J.T @ np.linalg.solve(J @ J.T + lam**2 * np.eye(6), K * err)
    
    # Format for Lua: {val1, val2, val3},
    print(f"    {{{qdot[0]:.8f}, {qdot[1]:.8f}, {qdot[2]:.8f}}},")
    
    # Update our 1-indexed dictionary
    theta[1] += qdot[0] * dt
    theta[2] += qdot[1] * dt
    theta[3] += qdot[2] * dt

print("}")
print("-" * 30)

final_pose = get_pose(theta)
print(f"Predicted Final Position: x={final_pose[0]:.2f}, y={final_pose[1]:.2f}, yaw={np.rad2deg(final_pose[5]):.2f} deg")